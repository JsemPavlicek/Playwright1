from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.









# Vývojářská konzole vs. Playwright:
# DOMContentLoaded (v konzoli jako domcontentload) odpovídá stavu 'domcontentloaded' v Playwrightu.
# Load (v konzoli jako load) odpovídá stavu 'load' v Playwrightu.
# Finish: To v konzoli označuje ukončení veškeré síťové aktivity a odpovídá stavu 'networkidle' v Playwrightu.

# domcontentloaded: Tento stav nastane, když HTML dokument byl plně načten a byl zpracován bez čekání na 
# styly, obrázky a jiné zdroje.

# load: Tento stav nastane, když je stránka plně načtena, včetně všech zdrojů jako jsou obrázky, styly, 
# skripty atd.

# networkidle: Tento stav nastane, když není žádná síťová aktivita