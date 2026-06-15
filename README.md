# Playwright + LangChain Browser Automation

A simple learning project that demonstrates:

- Browser automation using Playwright
- Extracting content from a website
- Summarizing extracted content using LangChain and Groq

## Files

- `test.py` - Opens the website and prints the page title
- `about.py` - Extracts content from the Ladder7 About page
- `summarize.py` - Generates a summary using Groq
- `about_content.txt` - Stores extracted website content

## Installation

```bash
pip install -r requirements.txt
playwright install
```

## Environment Variable

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
```

## Run

Extract content:

```bash
python about.py
```

Generate summary:

```bash
python summarize.py
```

## Learning Outcome

This project helped me learn:

- Playwright basics
- Browser automation
- Website content extraction
- LangChain integration
- Groq LLM usage
