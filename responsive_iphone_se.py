from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone_SE = p.devices['iPhone SE']
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(**iphone_SE)  # Použití unpacking (**) pro přidání vlastností z profilu zařízení
    page = context.new_page()
    page.goto('https://alza.cz')
    page.wait_for_timeout(10000)


print(iphone_SE)


# User agent je textový řetězec, který webový prohlížeč (nebo jiná aplikace) posílá webovému
# serveru při každém HTTP požadavku. Tento řetězec obsahuje informace o prohlížeči, operačním
# systému a někdy i o zařízení, které požadavek odesílá. Pomocí těchto informací může server
# přizpůsobit obsah nebo funkčnost webové stránky na základě typu prohlížeče nebo zařízení.

# Co obsahuje User Agent
# User agent řetězec může obsahovat různé informace, ale obvykle zahrnuje:
#
# Název a verze prohlížeče:
#
# Např. Chrome/91.0.4472.124, Firefox/89.0.
# Operační systém:
#
# Např. Windows NT 10.0; Win64; x64, Macintosh; Intel Mac OS X 10_15_7.
# Název a verze zařízení (u mobilních zařízení):
#
# Např. iPhone, Samsung Galaxy S10.
# Jazykové preference (někdy):
#
# Např. en-US, fr-FR.