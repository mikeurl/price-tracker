import requests
from bs4 import BeautifulSoup

def get_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Assume the price is within a span with class 'price'
    price = soup.find('span', class_='price').text
    return price

# Example usage
if __name__ == "__main__":
    url = 'http://example.com/product'
    price = get_price(url)
    print(f"The price is: {price}")
