from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://ladder7.in/about")

    page.wait_for_timeout(3000)

    text = page.text_content("body")

    with open("about_content.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("Content saved successfully")

    input("Press Enter to close...")

    browser.close()