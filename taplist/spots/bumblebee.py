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

            beer_elements = page.locator(".item")

            beer_menu = []

            count = beer_elements.count()
            for i in range(count):
                beer = beer_elements.nth(i)
                name = beer.locator(".item-name").locator("span").nth(1).text_content().strip()
                type = beer.locator(".item-name").locator(".item-category").text_content().strip() if beer.locator(".item-name").locator(".item-category").count() > 0 else "N/A"
                abv = beer.locator(".item-abv").text_content().strip() if beer.locator(".item-abv").count() > 0 else "N/A"
                brewery = beer.locator(".brewery").text_content().strip() if beer.locator(".brewery").count() > 0 else "N/A"
                description = beer.locator(".item-description").locator("p").text_content().strip() if beer.locator(".item-description").count() > 0 else "N/A"

                beer_menu.append({
                    'Name': name,
                    'ABV': abv,
                    'Brewery': brewery,
                    'Type': type,
                    'Description': description
                })

            browser.close()
            return beer_menu

    except Exception as e:
        print(f"Error fetching the webpage: {e}")
        return []

if __name__ == "__main__":
    url = "https://therustybumblebee.com/on-tap/"
    beers = scrape_beer_menu(url)

    if beers:
        print("\nBeer Menu:\n")
        for beer in beers:
            print(f"Name: {beer['Name']}")
            print(f"ABV: {beer['ABV']}")
            print(f"Brewery: {beer['Brewery']}")
            print(f"Type: {beer['Type']}\n")
            print(f"Description: {beer['Description']}")
    else:
        print("No beers found or an error occurred.")
