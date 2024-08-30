from playwright.sync_api import sync_playwright

text_dialog = []

def handle_dialog(dialog):
    message = dialog.message
    text_dialog.append(message)
    dialog.accept()
   #dialog.dismiss()


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
    # page.on("dialog", handle_dialog)
    page.on("dialog", handle_dialog)
    

    confirmbox.click()
    page.wait_for_timeout(5000)
    browser.close()
    print(text_dialog[0])


# Předání objektu dialogu:

# Když událost dialog nastane, Playwright automaticky vytvoří objekt dialog, který obsahuje všechny potřebné informace o tomto dialogu (např. jeho zprávu, typ dialogu atd.).
# Playwright automaticky předá tento objekt dialog jako argument do funkce handle_dialog, kterou jste zaregistrovali jako obslužnou funkci pro tuto událost.