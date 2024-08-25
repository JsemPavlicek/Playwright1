from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://demo.automationtesting.in/Index.html')
    # emailtxtbox = page.wait_for_selector("#email")
    emailtxtbox = page.locator("#email")

    emailtxtbox.type("test@seznam.cz")
    login_button = page.wait_for_selector("#enterimg")
    login_button.click()
    page.wait_for_timeout(5000)
    browser.close()

# WAIT_FOR_SELECTOR
# Defaulní nastavení wait_for_selector  je toto:    state = "visible"   a defaultní nastavení timeoutu je 30 sekund. Pokud se element během této doby nezobrazí na stránce, dojde k vyvolání výjimky TimeoutError.
# wait_for_selector se používá k čekání, dokud se element nezobrazí, ale po jeho zobrazení vrátí element, který můžete použít k dalším akcím. Nicméně, v novějších verzích Playwright API je preferováno použití locator pro interakci s elementy, protože je efektivnější.
# v kontextu wait_for_selector musí být prvek na stránce viditelný. Musí být viditelný v AKTUÁLNÍM zorném poli, viewportu prohlížeče. Nesmí být mimo oblast zobrazení. Nesmí mít CSS vlastnosti, které by ho skryly(visibility: hidden, display:none, opacity: 0), má pozitivní velikost (nemá 0px x 0 px), není překryt jiným elementem.
# stavy tedy mohou být tyto:
# visible: Čeká, dokud se element nestane viditelným v zorném poli prohlížeče.
# attached: Čeká, dokud je element připojený k DOM, bez ohledu na jeho viditelnost.
# hidden: Čeká, dokud je element skrytý na stránce, ale stále přítomný v DOM.
# detached: Čeká, dokud je element odstraněný z DOM.
# example: element = page.wait_for_selector("#my-element", state='hidden')



# LOCATOR
# Locator je Objekt, který slouží k vyhledávání a manipulaci s elementy na stránce. Je dynamický, což znamená, že element vyhledává pokaždé, když s ním chcete interagovat, takže automaticky reflektuje změny v DOM.
# Stabilita: Locators jsou robustnější vůči změnám na stránce. Pokud se stránka dynamicky mění, locators zajistí, že vždy pracujete s aktuálním stavem DOM.
# Efektivita: Locators vyhledávají elementy pouze tehdy, když s nimi chcete interagovat, což zlepšuje výkon a spolehlivost skriptů.
# Čekání na stav: Locators umožňují čekat na určité stavy elementů (např. viditelnost, přítomnost v DOM) před provedením akce.
# Když používáte metodu wait_for() na locator v Playwright Python, můžete specifikovat jeden z následujících stavů:

# visible: Čeká, dokud se element nestane viditelným.
# hidden: Čeká, dokud se element nestane skrytým nebo je odstraněn z DOM.
# attached: Čeká, dokud se element neobjeví v DOM, ale nemusí být viditelný.
# detached: Čeká, dokud není element odstraněn z DOM.
