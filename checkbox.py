from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Register.html')
    cookies = page.locator('button[aria-label="Consent"]')
    if cookies.count() > 0:
        cookies.click()
    checkbox1 = page.locator('input[value="Cricket"]')
    checkbox2 = page.locator('input[value="Movies"]')
    checkbox3 = page.locator('input[value="Hockey"]')

    checkbox1.check()
    checkbox2.check()
    checkbox3.check()
    page.wait_for_timeout(5000)
    browser.close()




# problém s Podmínkou if cookies:
# V Pythonu kontrola if cookies: pouze kontroluje, zda cookies není None nebo prázdný objekt. V Playwrightu metoda locator() vždy vrací objekt Locator, i když žádný odpovídající element na stránce nenajde. To znamená, že podmínka if cookies: bude vždy pravdivá, protože page.locator('button[aria-label="Consent"]') vždy vrátí Locator objekt, bez ohledu na to, zda daný element existuje nebo ne.

# Jak to udělat správně:
# Měli byste zkontrolovat, zda byl nalezen nějaký odpovídající element předtím, než provedete nějakou akci. Můžete to udělat například pomocí metody count()
# 
# Jak to funguje:
# page.locator('button[aria-label="Consent"]') vždy vrací Locator objekt, což je v podstatě reference na potenciální elementy na stránce. Tento Locator objekt sám o sobě neznamená, že elementy byly skutečně nalezeny.

# locator.count() je metoda, která vrací počet skutečně nalezených elementů, které odpovídají danému selektoru. Pokud žádný element neexistuje, vrátí count() hodnotu 0.

# if cookies.count() > 0 bude pravda pouze tehdy, pokud na stránce skutečně existuje alespoň jeden element, který odpovídá selektoru button[aria-label="Consent"]. Pokud takový element neexistuje, count() vrátí 0 a podmínka nebude splněna.

# if cookies: nekontroluje, zda jsou nalezeny nějaké odpovídající elementy, ale pouze, zda cookies není None. A protože locator() vždy vrací Locator objekt (i když prázdný), tato podmínka bude vždy splněna, což může vést k chybám, pokud se pokusíte kliknout na neexistující element.

# Locator v Playwrightu:

# locator() v Playwrightu vždy vrací objekt typu Locator, který představuje referenci na potenciální element nebo sadu elementů na stránce. Tento Locator objekt existuje, i když odpovídající HTML elementy na stránce nejsou přítomny.
# Jinými slovy, Locator je objekt, který vám umožňuje provádět akce (jako je kliknutí, získání textu atd.) na elementy, které odpovídají určitému selektoru, i když ve skutečnosti žádné takové elementy neexistují.
# Podmínka if cookies::
# Když používáte if cookies:, tato podmínka kontroluje, zda cookies (což je Locator objekt) existuje a není None. Vzhledem k tomu, že page.locator('button[aria-label="Consent"]') vždy vrací platný Locator objekt, podmínka if cookies: bude vždy vyhodnocena jako True, bez ohledu na to, zda odpovídající element existuje.
# Prázdný, ale platný objekt:
# Locator objekt není prázdný ve smyslu, že obsahuje potřebné informace a metody pro práci s potenciálními elementy. I když neexistuje žádný odpovídající HTML element, Locator stále existuje jako platný objekt, což způsobuje, že podmínka if cookies: bude pravdivá.
# Jak zjistit, zda element skutečně existuje:
# Abyste zjistili, zda element skutečně existuje na stránce, musíte zkontrolovat počet nalezených elementů pomocí metody count() nebo podobné metody:
