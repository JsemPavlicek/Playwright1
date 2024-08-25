from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.google.cz')
    page_title = page.title()
    page.wait_for_timeout(5000)
    print(f"Title of this webpage is : {page_title}")
    browser.close()


# Použití with pro uzavření prohlížeče: Používání with pro sync_playwright() je správné, 
#  automaticky uzavře prohlížeč. browser.close() se tedy v tomto kontextu používá k explicitnímu uzavření prohlížeče, 
# což je v pořádku, ale with zajistí, že se zdroje uvolní, pokud by došlo k chybě.
# V kontextu Playwrightu, with použijete k automatickému uzavření prohlížeče a všech otevřených stránek
# V Pythonu je with klíčové slovo používané k zajištění správného řízení zdrojů, jako jsou soubory,
#  síťové připojení, databázové připojení, nebo objekty, které potřebují otevřít a zavřít, přidělit a uvolnit. 
# Použití with je obvykle spojeno s kontejnery (context managers).