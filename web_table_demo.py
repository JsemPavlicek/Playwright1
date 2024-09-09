from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")
    cookies = page.locator('#ez-accept-all')
    if cookies.count() > 0:
        cookies.click()
        print("I clicked on the cookies")
    table = page.locator('table#customers')
    if table.count() > 0:
        print("I have found the table")
    one_row = table.locator('tr')
    number_of_rows = one_row.count()
    print(f"Number of rows is: {number_of_rows}")
    td_or_th= one_row.locator("td, th")
    for i in range(td_or_th.count()):
        print(f"{i + 1}:{td_or_th.nth(i).inner_text()}")


    browser.close()