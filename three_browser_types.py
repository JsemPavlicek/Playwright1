from playwright.sync_api import sync_playwright

test = 0
browsers = ["chromium", "firefox", "webkit"]
with sync_playwright() as p:
    three_browser_types =[p.chromium, p.firefox, p.webkit]
    for one_browser_type in three_browser_types:
        browser = one_browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.bazos.cz')
        browser.close()
        print(f'test number: {test + 1} was executed in browser: {browsers[test]}')
        test += 1