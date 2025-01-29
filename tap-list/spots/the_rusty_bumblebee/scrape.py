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

            beer_elements = page.locator(".section").nth(0).locator(".item")

            beer_menu = []

            count = beer_elements.count()
            for i in range(count):
                beer = beer_elements.nth(i)
                name = (
                    beer.locator(".item-name")
                    .locator("span")
                    .nth(1)
                    .text_content()
                    .strip()
                )
                beer_type = (
                    beer.locator(".item-name")
                    .locator(".item-category")
                    .text_content()
                    .strip()
                    if beer.locator(".item-name").locator(".item-category").count() > 0
                    else "N/A"
                )
                abv = (
                    beer.locator(".item-abv").text_content().strip()
                    if beer.locator(".item-abv").count() > 0
                    else "N/A"
                )
                brewery = (
                    beer.locator(".brewery").text_content().strip()
                    if beer.locator(".brewery").count() > 0
                    else "N/A"
                )
                description = (
                    beer.locator(".item-description")
                    .locator("p")
                    .text_content()
                    .strip()
                    if beer.locator(".item-description").count() > 0
                    else "N/A"
                )

                beer_menu.append(
                    {
                        "Name": f'"{name}"',
                        "ABV": f'"{abv}"',
                        "Brewery": f'"{brewery}"',
                        "Type": f'"{beer_type}"',
                        "Description": f"'{description.replace("\n", "")}'",
                    }
                )

            browser.close()

            beer_menu = sorted(beer_menu, key=lambda x: x["Name"])
            return beer_menu

    except Exception as e:
        print(f"Error fetching the webpage: {e}")
        return []


if __name__ == "__main__":
    url = "https://therustybumblebee.com/on-tap/"
    beers = scrape_beer_menu(url)

    print("taps:")

    if beers:
        for beer in beers:
            print(f"  - name: {beer['Name']}")
            print(f"    abv: {beer['ABV']}")
            print(f"    brewery: {beer['Brewery']}")
            print("    description: >")
            print(f"      {beer['Description']}")
            print(f"    type: {beer['Type']}")
    else:
        raise
