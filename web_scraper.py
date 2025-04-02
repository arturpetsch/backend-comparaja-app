import requests
from bs4 import BeautifulSoup

def scrape_prices_from_site():
    url = "https://www.example-marketplace.com/products"  # Substitua pelo site alvo
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = []
    for item in soup.find_all("div", class_="product"):
        name = item.find("h2").text.strip()
        price = item.find("span", class_="price").text.strip()
        products.append({"name": name, "price": price})

    return products