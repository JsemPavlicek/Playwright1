from playwright.sync_api import sync_playwright


def handle_download(download):
    file_location = './downloaded_file.zip'
    download.save_as(file_location)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.imacros.net/Automate/Downloads')
    page.on('download',handle_download)
    download_button = page.locator('a[href="/Content/Download.zip"]')
    download_button.click()
    page.wait_for_timeout(10000)

    browser.close()