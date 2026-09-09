# BrowseBrief

Scrape any webpage with Playwright and get an AI-generated summary using LangChain + Groq.

## Features

- Scrape any URL and extract clean, readable text
- Summarize the content using an LLM (Groq)
- Run scraping and summarizing together in one command

## Installation

```bash
git clone https://github.com/Arjunkalliyadath/playwright-langchain-browser-automation.git
cd playwright-langchain-browser-automation

pip install -r requirements.txt
playwright install chromium
```

## Configuration

Copy `.env.example` to `.env` and add your [Groq API key](https://console.groq.com/keys):

```bash
cp .env.example .env
```

```env
GROQ_API_KEY=your_api_key_here
```

If a model gives a "not found" error, run `python list_models.py` to see which models your key has access to.

## Usage

Scrape a page:
```bash
python scraper.py https://example.com
```

Summarize a saved file:
```bash
python summarizer.py example_com.txt
```

Or do both in one step:
```bash
python pipeline.py https://example.com -o summary.txt
```

## Testing

```bash
pip install -r requirements-dev.txt
pytest
```

## License

MIT — see [LICENSE](LICENSE).

## Author

**Arjun K**
- GitHub: [@Arjunkalliyadath](https://github.com/Arjunkalliyadath)
- Email: arjunkalliyadath2001@gmail.com
