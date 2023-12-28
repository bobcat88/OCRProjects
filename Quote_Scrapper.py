# Module Import
import requests
import csv
from bs4 import BeautifulSoup
# website to scrap
url = "http://quotes.toscrape.com/"
# url = input("Please type or paste URL from website to scrap:")

# use requests to get URL
response = requests.get(url)
# use BS4 to parse HTML
html = BeautifulSoup(response.text, 'html.parser')

# extract text and authors from html
extract_quote = html.find_all('span', class_="text")
extract_author = html.find_all('small', class_="author")

# put quotes and author in a list
quotes = list()
for quote in extract_quote:
    quotes.append(quote.text)
authors = list()
for author in extract_author:
    authors.append(author.text)

# Save author and quotes to a CSV file in local project (.py) location
with open('./AuthQuote.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(quotes, authors))