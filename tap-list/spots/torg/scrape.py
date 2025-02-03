from playwright.sync_api import sync_playwright


def scrape_beer_menu(url):
    try:
        with sync_playwright() as p:
            # Launch a headless browser
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            # Navigate to the URL
            page.goto(url)

            # Wait for the page to load completely
            page.wait_for_timeout(5000)  # Adjust the timeout if necessary

            beer_elements = page.locator("font").all()

            beer_menu = []

            for beer in beer_elements:

                print(beer.text_content())

                # name = (
                #     beer.locator(".bt_bb_menu_item_content")
                #     .locator(".bt_bb_menu_item_title")
                #     .text_content()
                #     .strip()
                # )

                # beer_info = (
                #     beer.locator(".bt_bb_menu_item_content")
                #     .locator(".bt_bb_menu_item_description")
                #     .text_content()
                #     .strip()
                #     .split(", ")
                # )

                # beer_type = beer_info[0]
                # abv = beer_info[1]

                # beer_menu.append(
                #     {
                #         "Name": f'"{name}"',
                #         "ABV": f'"{abv}"',
                #         "Type": f'"{beer_type}"',
                #     }
                # )

            browser.close()

            beer_menu = sorted(beer_menu, key=lambda x: x["Name"])
            return beer_menu

    except Exception as e:
        print(f"Error fetching the webpage: {e}")
        return []


if __name__ == "__main__":
    url = "https://www.torgbrewery.com/current-menu.html"
    beers = scrape_beer_menu(url)

    print("taps:")

    if beers:
        for beer in beers:
            print(f"  - name: {beer['Name']}")
            print(f"    abv: {beer['ABV']}")
            print(f"    type: {beer['Type']}")
    else:
        raise
