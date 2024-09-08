from playwright.sync_api import sync_playwright

def handle_ajax(response):
    if "https://www.plus2net.com/php_tutorial/dd-ajax.php?" in response.url:
        response_url = response.url
        response_status = response.status
        response_text = response.text()
        print(response_url)
        print(response_status)
        print(response_text)


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.plus2net.com/php_tutorial/ajax_drop_down_list-demo.php')
    cookies = page.locator('p.fc-button-label:has-text("Souhlas")')
    if cookies.count() > 0:
        cookies.click()
    select = page.locator('#s1')
    page.on("response", handle_ajax)
    select.select_option('2')
    page.wait_for_timeout(5000)
    browser.close()

# response.url - Vrací URL, na kterou byla odpověď přijata. Např.: response.url vrátí řetězec s plnou URL.
# response.status - Vrací stavový kód odpovědi (např. 200, 404, 500). Např.: response.status() vrátí 
# číslo stavového kódu odpovědi.
# response.text() - Vrací tělo odpovědi jako řetězec (text).