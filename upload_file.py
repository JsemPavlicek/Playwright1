from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.automationtesting.in/FileUpload.html")
    file_upload = './file_for_uploading.txt'
    file_upload_input = page.locator('input[id="input-4"]')
    file_upload_input.set_input_files(file_upload)
    page.wait_for_timeout(10000)
    browser.close()


# Relativní cesta ('./file_for_uploading.txt'):
#
# . (tečka) označuje aktuální adresář, tedy ten, ve kterém se nachází Python skript.
# Pokud je soubor file_for_uploading.txt ve stejném adresáři jako tvůj skript, použiješ právě tuto relativní cestu.
# Metoda set_input_files v Playwrightu slouží k nahrání souborů do webových formulářů, konkrétně do polí typu <input type="file">.
# locator.set_input_files(files)