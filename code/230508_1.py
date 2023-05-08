import requests
from bs4 import BeautifulSoup

def search_amazon(query):
    url = "https://www.amazon.com/s?k=" + query.replace(' ', '+')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all("div", {"class": "sg-col-inner"})

    for item in result:
        try:
            name = item.find("span", {"class": "a-size-medium a-color-base a-text-normal"}).get_text().strip()
            price = item.find("span", {"class": "a-offscreen"}).get_text().strip()
            print("Amazon: {} - {}".format(name, price))
        except:
            pass

def search_ebay(query):
    url = "https://www.ebay.com/sch/i.html?_nkw=" + query.replace(' ', '+')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    result = soup.find_all("div", {"class": "s-item__wrapper"})

    for item in result:
        try:
            name = item.find("h3", {"class": "s-item__title"}).get_text().strip()
            price = item.find("span", {"class": "s-item__price"}).get_text().strip()
            print("eBay: {} - {}".format(name, price))
        except:
            pass

query = input("Enter a product name: ")
search_amazon(query)
search_ebay(query)