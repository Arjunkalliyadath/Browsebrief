"""
pipeline.py
End-to-end: scrape a URL, then summarize the extracted content in one step.

Usage:
    python pipeline.py https://example.com
    python pipeline.py https://example.com -o summary.txt
    python pipeline.py https://example.com --headed
"""

import argparse
import sys

from scraper import scrape, slugify
from summarizer import get_llm, summarize


def main():
    parser = argparse.ArgumentParser(description="Scrape a URL and summarize it in one step.")
    parser.add_argument("url", help="URL to scrape and summarize")
    parser.add_argument("--headed", action="store_true",
                         help="Run with a visible browser window")
    parser.add_argument("-o", "--output", default=None,
                         help="Path to save the summary")
    parser.add_argument("-m", "--model", default=None,
                         help="Groq model to use (defaults to GROQ_MODEL / built-in default)")
    args = parser.parse_args()

    raw_path = f"{slugify(args.url)}.txt"

    print(f"Scraping {args.url} ...")
    try:
        scrape(args.url, raw_path, headless=not args.headed)
    except Exception as exc:
        print(f"Scrape failed: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Saved raw content to {raw_path}")
    print("Summarizing ...")

    with open(raw_path, encoding="utf-8") as f:
        content = f.read()

    try:
        llm = get_llm(args.model) if args.model else get_llm()
        summary = summarize(content, llm)
    except Exception as exc:
        print(f"Summarization failed: {exc}", file=sys.stderr)
        sys.exit(1)

    print("\n=== Summary ===\n")
    print(summary)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"\nSummary saved to {args.output}")


if __name__ == "__main__":
    main()
