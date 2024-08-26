from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.megaknihy.cz")
    cookies = page.locator(".CybotCookiebotDialogBodyButton").nth(3)
    cookies.click()
    books = page.locator(".category-tree-item ").nth(1)
    books.click()
    page.wait_for_timeout(5000)
    browser.close()

# .nth(index): Vybere prvek na základě jeho indexu (indexování začíná od 0). Například, pro výběr čtvrtého prvku použijete index 3.

