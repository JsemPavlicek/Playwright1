from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    try:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.gotoo('https://demo.automationtesting.in/Selectable.html')
        cookies = page.locator('p.fc-button-label:has-text("Consent")')

        if cookies.count() > 0:
            cookies.first.click()
        a_elements = page.locator('a')
        print(a_elements.count())
        for i in range(a_elements.count()):
            one_element = a_elements.nth(i)
            one_element_attribute = one_element.get_attribute('href')
            print(one_element_attribute)
        browser.close()
    except Exception as e:
        print(str(e))
    finally:
        print("Test has been executed")
    
    