# Playwright + LangChain Browser Automation

This project demonstrates browser automation using Playwright and website content summarization using LangChain and Groq.

## Project Overview

The application performs the following tasks:

1. Opens a website using Playwright.
2. Navigates to the Ladder7 website.
3. Extracts content from the About page.
4. Saves the extracted content into a text file.
5. Uses LangChain with Groq LLM to generate a summary of the extracted content.

---

## Workflow

Website (Ladder7 About Page)
        ↓
Playwright Browser Automation
        ↓
Content Extraction
        ↓
about_content.txt
        ↓
LangChain + Groq LLM
        ↓
Generated Summary

---

## Technologies Used

- Python
- Playwright
- LangChain
- Groq API
- python-dotenv

---

## Project Structure

```text
browser_automation/
│
├── test.py
├── about.py
├── summarize.py
├── about_content.txt
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Files Description

### test.py

Opens the Ladder7 website and prints the page title.

### about.py

Navigates to the About page, extracts website content, and stores it in `about_content.txt`.

### summarize.py

Reads the extracted content and generates a summary using Groq and LangChain.

### about_content.txt

Contains the extracted content from the About page.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Arjunkalliyadath/playwright-langchain-browser-automation.git
```

### Navigate to Project

```bash
cd playwright-langchain-browser-automation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Run the Project

### Open Website and Get Title

```bash
python test.py
```

### Extract Website Content

```bash
python about.py
```

### Generate Summary

```bash
python summarize.py
```

---

## Sample Output

```text
Key highlights of Ladder7 include:

• 99.9% uptime engineered
• 50+ MNC clients
• 250+ major deployments
• 50+ proof of concepts

Overall, Ladder7 is dedicated to helping organizations achieve digital transformation through technology and AI-driven solutions.
```

---

## Future Enhancements

- Build a LangChain Agent
- Answer user questions directly from website content
- Extract information from multiple pages
- Create a web-based AI assistant
- Integrate Retrieval-Augmented Generation (RAG)

---

## Author

Arjun K

AI/ML Intern Learning Project
