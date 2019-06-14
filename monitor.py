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

print(stock)

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
            item.notify('https://hooks.slack.com/services/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')
            print('notified')
            stock[key]=item
        newstock[key] = item
    stock = newstock

    sleep(60)




