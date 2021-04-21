#Name: Rodrigo Casa Nova

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import urllib.parse
urllib.parse.quote(':')
'%3A'


userCommand = input("Press Enter to check at some PCs prices.")
# setting the my_url variable with the website
my_url = "https://www.newegg.com/p/pl?d=gaming+desktop"
# opening connection, opening the page
uClient = uReq(my_url)
# reading the page and assigning the page_html variable to hold the website's content
page_html = uClient.read()
# closing connection with the website
uClient.close()
# html parse
page_soup = soup(page_html, "html.parser")

# grabs each products
containers = page_soup.findAll("div", {"class": "item-container"})
contain = containers[0]
container = containers[0]

# loop to get the item name, price, and shipping
for container in containers:
    item_price = container.findAll("li", {"class": "price-current"})
    price = item_price[0].text
    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text
    shipping_price = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_price[0].text.strip()
# print statements to output the name, price and shipping for each item
    print("Product Name: " + product_name)
    print("Product Price: " + price)
    print("Shipping Price: " + shipping)

userFeedback = input("\nDid you find what you were looking for? ")



