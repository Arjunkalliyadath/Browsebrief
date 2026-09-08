"""
summarizer.py
Summarizes a text file using Groq's LLM via LangChain.

Usage:
    python summarizer.py about_content.txt
    python summarizer.py about_content.txt -o summary.txt
    python summarizer.py about_content.txt -m llama-3.1-8b-instant
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
# Rough character budget so we stay comfortably inside the model's
# context window even for long scraped pages.
MAX_CHARS = 12000


def get_llm(model: str = DEFAULT_MODEL) -> ChatGroq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GROQ_API_KEY is not set. Copy .env.example to .env and add "
            "your key, or export GROQ_API_KEY in your shell."
        )
    return ChatGroq(model=model, api_key=api_key)


def summarize(content: str, llm) -> str:
    content = content.strip()
    if not content:
        raise ValueError("Input content is empty — nothing to summarize.")

    truncated_note = ""
    if len(content) > MAX_CHARS:
        content = content[:MAX_CHARS]
        truncated_note = "\n\n[Note: content truncated to fit the model's context window.]"

    prompt = (
        "You are a precise summarization assistant. Read the following "
        "webpage content and produce a clear, well-organized summary "
        "covering the company or page's purpose, offerings, and any "
        "notable facts or figures.\n\n"
        f"{content}"
    )

    response = llm.invoke(prompt)
    return response.content + truncated_note


def main():
    parser = argparse.ArgumentParser(description="Summarize a text file with Groq + LangChain.")
    parser.add_argument("input", nargs="?", default="about_content.txt",
                         help="Path to the text file to summarize (default: about_content.txt)")
    parser.add_argument("-o", "--output", default=None,
                         help="Optional path to save the summary")
    parser.add_argument("-m", "--model", default=DEFAULT_MODEL,
                         help=f"Groq model to use (default: {DEFAULT_MODEL})")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    content = input_path.read_text(encoding="utf-8")

    try:
        llm = get_llm(args.model)
        summary = summarize(content, llm)
    except Exception as exc:
        print(f"Summarization failed: {exc}", file=sys.stderr)
        sys.exit(1)

    print(summary)

    if args.output:
        Path(args.output).write_text(summary, encoding="utf-8")
        print(f"\nSummary saved to {args.output}")


if __name__ == "__main__":
    main()
