from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    cookies = page.locator('button[aria-label="Consent"]')
    if cookies:
        cookies.click()

    radio_button = page.locator('input[value="FeMale"]')
    label = radio_button.locator('..')
    # label_text = label.inner_text()
    label_text = label.text_content()
    radio_button.check()
    if radio_button.is_checked:
        print(f'radio_button has been checked and label of this radio button is {label_text}')
    else:
        print("radio_button hasn't been checked")
    page.wait_for_timeout(10000)
    browser.close()

# Selektor '..' používá XPath styl navigace, kde .. znamená "nadřazený element". V tomto případě se přesunete z <input> na jeho přímého rodiče, což by měl být element <label>.
# inner_text vs. text_content v Playwright
# Obě metody, inner_text() a text_content(), slouží k získání textového obsahu z elementu na webové stránce, ale liší se v tom, jak s textem nakládají. Zde je podrobné vysvětlení obou metod:

# inner_text()
# Co dělá:
# inner_text() vrací viditelný text uvnitř elementu tak, jak je vykreslený na stránce. To znamená, že vrací text, který by uživatel skutečně viděl v prohlížeči.
# Ignoruje skrytý text. Pokud má element skrytý text (např. pomocí CSS stylu display: none;), inner_text() tento text nevrátí.
# použít:
# Když potřebujete získat text tak, jak je zobrazený uživateli na stránce, bez ohledu na skryté nebo neviditelné části.

# text_content()
# Co dělá:
# text_content() vrací veškerý textový obsah uvnitř elementu, včetně textu, který není viditelný (např. text uvnitř skrytých elementů).