"""
scraper.py
Generic Playwright-based web scraper.

Extracts clean, human-readable text from any webpage and saves it to a
file. Unlike a naive `text_content("body")` call, this strips out
<script>, <style>, <noscript>, <svg>, and <iframe> elements first and
reads rendered (visible) text, so you don't end up with raw CSS/JS
source mixed into your output.

Usage:
    python scraper.py https://example.com
    python scraper.py https://example.com -o output.txt
    python scraper.py https://example.com --headed
"""

import argparse
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

DEFAULT_URL = "https://ladder7.in/about"
DEFAULT_TIMEOUT_MS = 15000


def slugify(url: str) -> str:
    """Turn a URL into a filesystem-safe slug, e.g. for default filenames."""
    parsed = urlparse(url)
    slug = f"{parsed.netloc}{parsed.path}".strip("/")
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", slug).strip("_")
    return slug or "page"


def extract_clean_text(page) -> str:
    """Remove non-content elements, then return the page's visible text."""
    page.evaluate(
        """
        () => {
            document
                .querySelectorAll('script, style, noscript, svg, iframe')
                .forEach(el => el.remove());
        }
        """
    )
    text = page.inner_text("body")
    # Collapse the extra blank lines left behind by removed elements.
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def scrape(url: str, output_path: str, headless: bool = True,
           timeout_ms: int = DEFAULT_TIMEOUT_MS) -> str:
    """Scrape a URL and write its clean text content to output_path."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        try:
            page = browser.new_page()
            try:
                page.goto(url, timeout=timeout_ms, wait_until="domcontentloaded")
                page.wait_for_load_state("networkidle", timeout=timeout_ms)
            except PlaywrightTimeoutError:
                # Some pages (ads, trackers, websockets) never go fully
                # idle. The DOM is already loaded, so we can continue.
                pass

            text = extract_clean_text(page)
            Path(output_path).write_text(text, encoding="utf-8")
        finally:
            browser.close()

    return output_path


def main():
    parser = argparse.ArgumentParser(description="Extract clean text from a webpage.")
    parser.add_argument("url", nargs="?", default=DEFAULT_URL,
                         help=f"URL to scrape (default: {DEFAULT_URL})")
    parser.add_argument("-o", "--output", default=None,
                         help="Output file path (default: <slug>.txt)")
    parser.add_argument("--headed", action="store_true",
                         help="Run with a visible browser window (default: headless)")
    args = parser.parse_args()

    output_path = args.output or f"{slugify(args.url)}.txt"
    headless = not args.headed and os.getenv("HEADLESS", "true").lower() != "false"

    try:
        path = scrape(args.url, output_path, headless=headless)
    except Exception as exc:
        print(f"Failed to scrape {args.url}: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Content saved to {path}")


if __name__ == "__main__":
    main()
