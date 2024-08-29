from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    cookies = page.locator('button[aria-label="Consent"]')
    if cookies.count() > 0:
        cookies.click()
    button = page.locator('a[href="#CancelTab"]')
    button.click()
    confirmbox = page.locator('[onclick="confirmbox()"]')
    # page.on("dialog", lambda dialog: dialog.accept())
    page.on("dialog", lambda dialog: dialog.dismiss())

    confirmbox.click()
    page.wait_for_timeout(5000)
    browser.close()

# pokud s dialogem souhlasím, je použita metoda accept(). Pokud nesoulasím, je použita metoda dismiss().