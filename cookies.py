from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://redbus.in")
    page.context.clear_cookies()
    new_cookies = [{
        "name": "Ravi",
        "value": "126dpb",
        "domain": "redbus.in",
        "path": "/"
    }]
    page.context.add_cookies(new_cookies)

    # V Playwrightu se cookies předávají jako seznam slovníků (list of dictionaries), 
    # protože můžete přidávat více cookies najednou. Každý slovník v seznamu představuje jednu cookie,
    #  která má atributy jako name, value, domain, atd.

    page.screenshot(path="redbus.png")
    page.screenshot(path="redbusfullpage.png", full_page=True)