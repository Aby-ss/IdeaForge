import requests

# Replace with your Shopify store's API credentials
API_KEY = 'YOUR_API_KEY'
PASSWORD = 'YOUR_PASSWORD'
SHOP_URL = 'YOUR_SHOPIFY_STORE_URL'
API_VERSION = '2021-10'

# Authenticate with Shopify API
auth = (API_KEY, PASSWORD)

# Function to fetch data from Shopify API
def fetch_shopify_data(endpoint):
    url = f'https://{SHOP_URL}/admin/api/{API_VERSION}/{endpoint}.json'
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error fetching data from {url}: {response.status_code}')
        return None

# Function to gather store information
def get_store_info():
    shop_info = fetch_shopify_data('shop')
    if shop_info:
        print(f"Store Name: {shop_info['shop']['name']}")
        print(f"Email: {shop_info['shop']['email']}")
        print(f"Domain: {shop_info['shop']['domain']}")
        # Add more store details as needed

# Function to gather product information
def get_product_info():
    products = fetch_shopify_data('products')
    if products:
        for product in products['products']:
            print(f"Product Name: {product['title']}")
            print(f"Description: {product['body_html']}")
            print(f"Price: {product['variants'][0]['price']}")
            # Add more product details as needed

# Main function
def main():
    print("Fetching Store Information:")
    get_store_info()

    print("\nFetching Product Information:")
    get_product_info()