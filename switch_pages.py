from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    cookies = page.locator('button[aria-label="Consent"]')
    if cookies.count() > 0:
        cookies.click()
    click_btn = page.locator('a[href="http://www.selenium.dev"] > button')
    click_btn.click()
    page.wait_for_timeout(20000)
    pages = context.pages
    print(len(pages))
    new_page = pages[1]
    new_page.bring_to_front()
    page.wait_for_timeout(5000)
    for one_page in pages:
        print(f"page: {one_page} and page Title: {one_page.title()}")
    new_page.close()
    page.close()
    browser.close()