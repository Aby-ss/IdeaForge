import requests
from bs4 import BeautifulSoup

# URL of the website to scrape (replace with your desired website)
url = "https://www.example.com/products"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find product containers (modify this based on the website's structure)
    product_containers = soup.find_all("div", class_="product-container")

    if not product_containers:
        print("No product containers found on the page.")
    else:
        # Iterate through the product containers
        for container in product_containers:
            # Find product title, price, and link (modify this based on the website's structure)
            product_title = container.find("h2", class_="product-title").text.strip()
            product_price = container.find("span", class_="product-price").text.strip()
            product_link = container.find("a", class_="product-link")["href"]

            # Display product information
            print("Product Title:", product_title)
            print("Price:", product_price)
            print("Product Link:", product_link)
            print("-" * 50)
else:
    print("Failed to retrieve the webpage.")