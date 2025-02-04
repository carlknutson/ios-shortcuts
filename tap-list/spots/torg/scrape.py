from playwright.sync_api import sync_playwright


def scrape_beer_menu(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            page.goto(url)

            page.wait_for_timeout(5000)

            beer_elements = page.locator("font").all()

            menu = []

            for line in beer_elements:
                menu.append(line.text_content().strip())

            browser.close()

            return menu

    except Exception as e:
        print(f"Error fetching the webpage: {e}")
        return []


if __name__ == "__main__":
    url = "https://www.torgbrewery.com/current-menu.html"
    lines = scrape_beer_menu(url)

    print("menu:")

    for line in lines:
      print(f"  - {line}")
