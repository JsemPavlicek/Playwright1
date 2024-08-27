from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    # cookies = page.locator('//button[text()="Consent"]')
    # cookies = page.locator('button:has-text("Consent")') nelze jej takto použít, na stránce jsou dvě tlačítka s tímto textem.
    cookies = page.locator('button[aria-label="Consent"]')
    if cookies:
        cookies.click()
    page.select_option('//select[@id="Skills"]',"Python")
    page.wait_for_timeout(5000)
    browser.close()

# Použití textového selektoru: Pokud chceš jednoduše vybrat tlačítko na základě jeho textu, můžeš použít následující zápis:
# cookies = page.locator('button:has-text("Consent")')
# XPath selektory mají tendenci být méně efektivní než jiné typy selektorů, zejména na složitých nebo velkých stránkách, 
# kde může prohledávání celého DOM stromu trvat déle.

# Důvody, proč může docházet k chybám:
# Pomalejší vyhledávání: XPath selektory často prohledávají celý DOM strom, což může být pomalejší než jiné selektory. Pokud Playwright nenajde prvek včas (během daného časového limitu), může vyhodit chybu, že prvek nebyl nalezen.

# Nenačtené prvky: Pokud se stránka načítá asynchronně (např. tlačítko se zobrazí po nějaké akci nebo po načtení jiného obsahu), XPath selektor může selhat, pokud prvek ještě není v DOM stromu přítomen.

# Nepřesnost selektoru: XPath selektory mohou být obecné, což může vést k nechtěnému výběru jiných prvků nebo žádného prvku, pokud není selektor přesně definován.

# Řešení:
# Použití jednodušších selektorů: Pokud je to možné, přepni na jednodušší a rychlejší selektory, jako jsou textové nebo atributové selektory. Tyto selektory jsou obvykle rychlejší a přesnější.


