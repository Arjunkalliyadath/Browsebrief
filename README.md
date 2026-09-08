# BrowseBrief

**Point it at a URL. Get back a clean AI summary.**

BrowseBrief is a small toolkit that combines [Playwright](https://playwright.dev/python/) browser automation with [LangChain](https://python.langchain.com/) + [Groq](https://groq.com/) to scrape any webpage, strip it down to clean readable text, and summarize it with an LLM — all from the command line.

It started as a learning project (Playwright basics → content extraction → LangChain/Groq integration) and has grown into a small, reusable, tested tool.

## Features

- 🌐 **Scrape any URL** — not hardcoded to one site
- 🧹 **Clean extraction** — strips `<script>`, `<style>`, and other noise before pulling text, so you get readable content instead of raw CSS/JS
- 🤖 **AI summaries** — powered by Groq's LLM via LangChain
- 🔗 **One-command pipeline** — scrape + summarize in a single call
- 🛡️ **Error handling** — missing API keys, timeouts, and missing files fail with clear messages instead of crashes
- ✅ **Unit tested** — core logic is covered by `pytest`, with CI on every push
- ⚙️ **Configurable** — headless mode, model choice, and output paths are all flags/env vars, not hardcoded

## Project Structure

```
browsebrief/
├── scraper.py          # Scrape a URL → clean text file
├── summarizer.py        # Summarize a text file with Groq + LangChain
├── pipeline.py           # Scrape + summarize in one step
├── smoke_test.py         # Quick sanity check that Playwright works
├── tests/                 # Unit tests (no browser/API key required)
├── .github/workflows/      # CI: runs tests on every push/PR
├── requirements.txt
├── requirements-dev.txt
└── .env.example
```

## Installation

```bash
git clone https://github.com/Arjunkalliyadath/playwright-langchain-browser-automation.git
cd playwright-langchain-browser-automation

pip install -r requirements.txt
playwright install chromium
```

## Configuration

Copy the example environment file and add your [Groq API key](https://console.groq.com/keys):

```bash
cp .env.example .env
```

```env
GROQ_API_KEY=your_api_key_here

# Optional overrides
GROQ_MODEL=llama-3.3-70b-versatile
HEADLESS=true
```

## Usage

**Scrape a page:**

```bash
python scraper.py https://ladder7.in/about
# → saves clean text to ladder7_in_about.txt

python scraper.py https://example.com -o output.txt --headed
```

**Summarize a saved file:**

```bash
python summarizer.py ladder7_in_about.txt
python summarizer.py ladder7_in_about.txt -o summary.txt -m llama-3.1-8b-instant
```

**Or do both in one step:**

```bash
python pipeline.py https://ladder7.in/about -o summary.txt
```

**Sanity-check your Playwright install:**

```bash
python smoke_test.py https://example.com
```

## Testing

Unit tests cover the pure logic (URL slugging, summarization/truncation behavior) without needing a browser or a live API key:

```bash
pip install -r requirements-dev.txt
pytest
```

## What Changed From the Original Version

This started as `about.py` / `test.py` / `practice.py` / `summarize.py`, hardcoded to one site. Along the way:

- Added the missing `requirements.txt` (the README referenced it, but it never existed)
- Fixed text extraction pulling in raw CSS/JS instead of clean page content
- Fixed a typo in the summarization prompt
- Added error handling around missing API keys, missing files, and page timeouts (scripts no longer crash with a raw traceback or hang with an unclosed browser)
- Generalized everything to work with any URL instead of one hardcoded site
- Merged `test.py` and `practice.py`, which were identical, into a single `smoke_test.py`
- Added a `pipeline.py` for a one-command scrape-and-summarize flow
- Added truncation for long pages so they don't blow past the model's context window
- Added unit tests and a CI workflow

## Roadmap / Ideas

- [ ] Support batch summarization of a list of URLs
- [ ] Optional Markdown/JSON output for summaries
- [ ] Swap in an async Playwright backend for concurrent scraping
- [ ] Add a `--extract-links` mode for crawling multiple pages on a site

## License

MIT — see [LICENSE](LICENSE).
