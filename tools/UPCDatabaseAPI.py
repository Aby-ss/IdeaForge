import requests
from rich.panel import Panel
from rich.traceback import install
install(show_locals=True)

# UPC API Base URL
UPC_API_BASE_URL = "https://api.upcdatabase.org/product/"

# Replace 'YOUR_API_KEY' with your actual API key (if required)
API_KEY = 'CF459CF8D921A528FC11B789FBDB41C0'

# Function to fetch product information using UPC code
def get_product_info(upc_code):
    url = f"{UPC_API_BASE_URL}{upc_code}"
    headers = {"Content-Type": "application/json"}
    params = {"apikey": API_KEY}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to display product information in a rich panel
def display_product_info(product_info):
    panel = Panel.fit("[bold]Product Information:[/bold]\n", title="Product Details", border_style="cyan")
    
    for key, value in product_info.items():
        panel += f"[cyan]{key.capitalize()}: {value}[/cyan]\n"

    return panel

if __name__ == "__main__":
    upc_code = input("Enter the UPC code: ")

    if upc_code:
        product_info = get_product_info(upc_code)

        if product_info:
            panel = display_product_info(product_info)
            print(panel)
        else:
            print("Product not found or API request failed.")
    else:
        print("Please enter a UPC code.")