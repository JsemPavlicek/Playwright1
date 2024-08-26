from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.megaknihy.cz/")
    cookies = page.locator(".CybotCookiebotDialogBodyButton").nth(3)
    cookies.click()
    page.wait_for_timeout(40000)
    search_input = page.locator('//input[@placeholder="Zadejte hledaný titul, autora"]')
    search_button = page.locator('//button[text()="Vyhledat"]')
    search_input.type("Španělština")
    search_button.click()
    page.wait_for_timeout(5000)
    browser.close()

# XPath (XML Path Language) je dotazovací jazyk pro navigaci ve strukturovaných dokumentech, jako je XML nebo HTML.