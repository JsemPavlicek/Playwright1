# device emulation iPad Mini and testing domcontentloaded event on Alza.cz

from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    ipad_mini = p.devices["iPad Mini"]
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(**ipad_mini)
    page = context.new_page()
    start_time = time.time()
    page.goto("https://alza.cz", wait_until="domcontentloaded")
    end_time = time.time()
    domcontentloaded_time = end_time - start_time
    print(f"domcontentloaded_time is: {domcontentloaded_time}")
    browser.close()



