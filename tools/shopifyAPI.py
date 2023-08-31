import requests

# Replace with your actual Shopify store domain and API key
SHOP_DOMAIN = 'your-shop-name.myshopify.com'
API_KEY = 'your-api-key'
API_PASSWORD = 'your-api-password'

def get_shop_info():
    url = f'https://{SHOP_DOMAIN}/admin/api/2021-07/shop.json'
    response = requests.get(url, auth=(API_KEY, API_PASSWORD))
    data = response.json()
    return data['shop']

def get_orders():
    url = f'https://{SHOP_DOMAIN}/admin/api/2021-07/orders.json'
    response = requests.get(url, auth=(API_KEY, API_PASSWORD))
    data = response.json()
    return data['orders']

# Example usage
shop_info = get_shop_info()
print("Shop Information:", shop_info)

orders = get_orders()
print("Orders:", orders)