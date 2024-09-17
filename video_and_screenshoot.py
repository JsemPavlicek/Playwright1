from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='.') # uloží video do aktuální složky
    page = context.new_page()
    page.goto('https://alza.cz')
    page.wait_for_timeout(5000)
    page.screenshot(path='screenshot_alza.png')
    cookies = page.locator('a[href="javascript:Alza.Web.Cookies.acceptAllCookies();"]')
    if cookies.count() > 0:
        cookies.click()
        page.wait_for_timeout(5000)
    context.close()
    browser.close()

