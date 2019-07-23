# -*- coding: utf-8 -*-'
from collections import Counter
import math, random, csv, json, re
from bs4 import BeautifulSoup
import requests

def process(date, symbol, price):
        print(date, symbol, price)

print("tab delimited stock prices:")

with open('tab_delimited_stock_prices.txt', 'r', encoding='utf8',newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    # reader = csv.reader(codecs.iterdecode(f, 'utf-8'), delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        process(date, symbol, closing_price)

print()

print("colon delimited stock prices:")

with open('colon_delimited_stock_prices.txt', 'r', encoding='utf8',newline='') as f:
    reader = csv.DictReader(f, delimiter=':')
    # reader = csv.DictReader(codecs.iterdecode(f, 'utf-8'), delimiter=':')
    for row in reader:
        date = row["date"]
        symbol = row["symbol"]
        closing_price = float(row["closing_price"])
        process(date, symbol, closing_price)

print()

print("writing out comma_delimited_stock_prices.txt")

today_prices = { 'AAPL' : 90.91, 'MSFT' : 41.68, 'FB' : 64.5 }

with open('comma_delimited_stock_prices.txt','w', encoding='utf8',newline='') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])



url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')
print(soup)


first_paragraph = soup.find('p')        # or just soup.p
print(first_paragraph)
first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()


assert first_paragraph_words == ['This', 'is', 'the', 'first', 'paragraph.']

first_paragraph_id = soup.p['id']       # raises KeyError if no 'id'
first_paragraph_id2 = soup.p.get('id')  # returns None if no 'id'


assert first_paragraph_id == first_paragraph_id2 == 'p1'

all_paragraphs = soup.find_all('p')  # or just soup('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]


assert len(all_paragraphs) == 2
assert len(paragraphs_with_ids) == 1

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]


assert important_paragraphs == important_paragraphs2 == important_paragraphs3
assert len(important_paragraphs) == 1


