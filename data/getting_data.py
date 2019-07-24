# -*- coding: utf-8 -*-'
from collections import Counter
import math, random, csv, json, re
from bs4 import BeautifulSoup
import requests
from matplotlib import pyplot as plt

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

first_paragraph_id = soup.p['id']       # raises KeyError if no 'id'
first_paragraph_id2 = soup.p.get('id')  # returns None if no 'id'

all_paragraphs = soup.find_all('p')  # or just soup('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')]

important_paragraphs = soup('p', {'class' : 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])]



######
#
# BOOKS ABOUT DATA
#
######

#def is_video(td):
#    """it's a video if it has exactly one pricelabel, and if
#    the stripped text inside that pricelabel starts with 'Video'"""
#    pricelabels = td('span', 'pricelabel')
#    return (len(pricelabels) == 1 and
#            pricelabels[0].text.strip().startswith("Video"))
#
#def book_info(td):
#    """given a BeautifulSoup <td> Tag representing a book,
#    extract the book's details and return a dict"""
#    
#    title = td.find("div", "thumbheader").a.text
#    by_author = td.find('div', 'AuthorName').text
#    authors = [x.strip() for x in re.sub("^By ", "", by_author).split(",")]
#    isbn_link = td.find("div", "thumbheader").a.get("href")
#    isbn = re.match("/product/(.*)\.do", isbn_link).groups()[0]
#    date = td.find("span", "directorydate").text.strip()
#    
#    return {
#        "title" : title,
#        "authors" : authors,
#        "isbn" : isbn,
#        "date" : date
#    }

#from time import sleep
#
#base_url = "http://shop.oreilly.com/category/browse-subjects/" + \
#       "data.do?sortby=publicationDate&page="

books = []

books.append({"title":"Data Science from scratch", "year":2014})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2017})
books.append({"title":"Data Science from scratch", "year":2017})
books.append({"title":"Data Science from scratch", "year":2017})
books.append({"title":"Data Science from scratch", "year":2017})
books.append({"title":"Data Science from scratch", "year":2017})
books.append({"title":"Data Science from scratch", "year":2017})
books.append({"title":"Data Science from scratch", "year":2017})
books.append({"title":"Data Science from scratch", "year":2017})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2016})
books.append({"title":"Data Science from scratch", "year":2014})
books.append({"title":"Data Science from scratch", "year":2014})
books.append({"title":"Data Science from scratch", "year":2014})
books.append({"title":"Data Science from scratch", "year":2014})
books.append({"title":"Data Science from scratch", "year":2013})
books.append({"title":"Data Science from scratch", "year":2013})
books.append({"title":"Data Science from scratch", "year":2013})
books.append({"title":"Data Science from scratch", "year":2013})
books.append({"title":"Data Science from scratch", "year":2012})
books.append({"title":"Data Science from scratch", "year":2012})
books.append({"title":"Data Science from scratch", "year":2012})
books.append({"title":"Data Science from scratch", "year":2012})
books.append({"title":"Data Science from scratch", "year":2011})
books.append({"title":"Data Science from scratch", "year":2011})
books.append({"title":"Data Science from scratch", "year":2011})
books.append({"title":"Data Science from scratch", "year":2011})
books.append({"title":"Data Science from scratch", "year":2010})
books.append({"title":"Data Science from scratch", "year":2010})
books.append({"title":"Data Science from scratch", "year":2010})
books.append({"title":"Data Science from scratch", "year":2009})

#for page_num in range(1, 31 + 1):
#    print ("souping page", page_num)
#    url = base_url + str(page_num)
#    soup = BeautifulSoup(requests.get(url).text, 'html5lib')
#        
#    for td in soup('td', 'thumbtext'):
#        if not is_video(td):
#            books.append(book_info(td))
#            
#    print(books)
#    # now be a good citizen and respect the robots.txt!
#    sleep(0.5)


def get_year(book):
    """book["date"] looks like 'November 2014' so we need to 
    split on the space and then take the second piece"""
    return int(book["year"])


    # 2014 is the last complete year of data (when I ran this)
year_counts = Counter(get_year(book) for book in books
                      if get_year(book) <= 2017)

years = sorted(year_counts)
print('years:', years)
book_counts = [year_counts[year] for year in years]
plt.bar([x - 0.5 for x in years], book_counts)
plt.xlabel("year")
plt.ylabel("# of data books")
plt.title("Data is Big!")
plt.show()


#Using APIs

#parsing my github repo

endpoint = "https://api.github.com/users/jaspreetRFSingh/repos"

repos = json.loads(requests.get(endpoint).text)
num_of_repos = len(repos)
for i in range(num_of_repos):    
    print(repos[i]["name"])

from dateutil.parser import parse


dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

print(month_counts, weekday_counts)


