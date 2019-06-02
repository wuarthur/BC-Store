import requests
from bs4 import BeautifulSoup
from products import  Product
from time import sleep


products=[]
stock={}

#first run
response = requests.get('https://www.bccannabisstores.com/collections/bottles-drops')
soup = BeautifulSoup(response.text)
items_divs = mydivs = soup.findAll("div", {"class": "productitem"})
for div in items_divs:
    item = Product(div)
    products.append(item)
    key = item.name + item.price
    if key in stock:
        print(item)
    stock[key] = item

#monitoring
while True:
    newstock={}
    response = requests.get('https://www.bccannabisstores.com/collections/bottles-drops')
    soup = BeautifulSoup(response.text)
    items_divs=mydivs = soup.findAll("div", {"class": "productitem"})
    for div in items_divs:
        item = Product(div)
        products.append(item)
        key = item.name + item.price
        if key in stock:
            pass
        else:
            #todo notify this item
            print('notified')
            stock[key]=item
        newstock[key] = item
    stock = newstock

    sleep(60)




