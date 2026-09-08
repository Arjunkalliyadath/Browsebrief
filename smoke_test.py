"""
smoke_test.py
Minimal Playwright sanity check — launches a browser, opens a page, and
prints its title. Useful for confirming your Playwright install works
before running the scraper or pipeline.

(Replaces the old test.py / practice.py, which were identical scripts.)

Usage:
    python smoke_test.py
    python smoke_test.py https://example.com
"""

import sys

from playwright.sync_api import sync_playwright


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else "https://ladder7.in"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        try:
            page = browser.new_page()
            page.goto(url)
            print(f"Title: {page.title()}")
            input("Press Enter to close...")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
