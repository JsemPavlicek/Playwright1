from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(60000)
    user_input = page.locator('input[name="username"]')
    if user_input.count() > 0:
        print("locator was founded")
    else:
        print("Locator wasn't founded")
    user_input.type("Admin")
    user_password = page.locator("input[type='password']")
    user_password.type("admin123")
    login_button = page.locator('button[type="submit"]')
    login_button.click()
    page.wait_for_timeout(5000)
    browser.close()


# použití metody count je možné pouze na objektech typu locator
# Vytvoření locatoru pro všechny 'button' prvky
#buttons = page.locator('button')
# Počítá, kolik 'button' prvků se na stránce nachází
# count = buttons.count()

# nebo např. Vytvoření locatoru pro všechny 'button' prvky
# buttons = page.locator('button')
# Kontrola, zda existuje alespoň jeden 'button' prvek
# if buttons.count() > 0:

# count() nemůže být použito na objektu vráceném z wait_for_selector()
# metoda count() na objektu typu Locator v Playwrightu vrací vždy číslo. Toto číslo představuje počet prvků, 
# které odpovídají danému selektoru na stránce.


