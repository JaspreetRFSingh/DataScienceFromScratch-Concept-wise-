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
