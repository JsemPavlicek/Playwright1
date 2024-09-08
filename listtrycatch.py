from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Selectable.html')
    b_tags = page.locator('ul b')
    number_of_b_tags = b_tags.count()
    print(number_of_b_tags)
    for i in range(number_of_b_tags):
        print(f"{i + 1}: {b_tags.nth(i).inner_text()}")


    browser.close()

# přes lokátor nelze iterovat jako přes list. Lze ale k jednotlivým prvkům v něm přistupovat pomocí nth(index).
# funguje totiž jako ukazatel na objekty