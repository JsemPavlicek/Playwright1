from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Selectable.html')
    page.wait_for_load_state('networkidle')
    cookies = page.locator('p.fc-button-label:has-text("Consent")').first

    if cookies.count() > 0:
        cookies.click()
    switch_to = page.locator('a[href="SwitchTo.html"]').nth(0)
    switch_to.hover()
    page.wait_for_timeout(5000)
    #switch_to.click()
    # page.wait_for_timeout(5000)
    #switch_to.dblclick()
    switch_to.press('Enter')
    page.wait_for_timeout(5000)

    browser.close()
