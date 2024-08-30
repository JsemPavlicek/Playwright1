from playwright.sync_api import sync_playwright

def handle_dialog(dialog):
    message = dialog.message
    dialog.accept("Pavel")
    print(dialog.message)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    cookies = page.locator('button[aria-label="Consent"]')
    if cookies.count() > 0:
        cookies.click()
    alert_with_textbox = page.locator('a:has-text("Alert with Textbox ")')
    alert_with_textbox.click()
    prompt_button = page.locator('button[onclick="promptbox()"]')
    page.on("dialog", handle_dialog)
    prompt_button.click()
    page.wait_for_timeout(5000)
    browser.close()

# Práce s dialogem prompt:

# V dialogu typu prompt můžete použít dialog.accept(text) k zadání textu do vstupního pole dialogu a jeho potvrzení.
# Pokud chcete dialog odmítnout, můžete použít dialog.dismiss().