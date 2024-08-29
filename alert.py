from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Alerts.html')
    cookies = page.locator('button[aria-label="Consent"]')
    if cookies.count() > 0:
        cookies.click()
    alert_with_ok = page.locator('[href="#OKTab"]')
    alert_with_ok.click()
    dialog_alert = page.locator('[onclick="alertbox()"]')
    page.on("dialog", lambda dialog: dialog.accept())
    dialog_alert.click()
    page.wait_for_timeout(5000)
    browser.close()

# alert(): Toto je jednoduchý dialog, který zobrazuje zprávu a tlačítko OK. Po stisknutí tlačítka OK dialog zmizí a skript pokračuje v provádění.

# javascript
# alert('This is an alert message!');
# V tomto příkladu se zobrazí malý dialog s textem „This is an alert message!“ a jediným tlačítkem OK.
# alert() vždy zobrazuje pouze jedno tlačítko OK.

# V Pythonu se anonymní funkce, tedy funkce bez jména, vytvářejí pomocí klíčového slova lambda.
# lambda arguments: expression
# add = lambda x, y: x + y
# print(add(2, 3))  # Výstup bude 5

