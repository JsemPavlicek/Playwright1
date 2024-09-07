from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://redbus.in")
    cookies = page.context.cookies()
    print(cookies)


# V Playwrightu je page.context.cookies() metoda,
# která získá cookies pro konkrétní page. Na druhé straně context.cookies() je metoda,
# která získá cookies pro celý browser context.