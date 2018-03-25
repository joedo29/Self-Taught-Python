# Author: Joe Do
# Date: March 01, 2018

# Import four library below to read javascript
import sys
from PyQt4.QtGui import QApplication
from PyQt4.Qtcore import QUrl
from PyQt4.QWebKit import QWebPage

import bs4 as bs
import urllib.request
import pandas as pd

# class Client(QWebPage):
#     def __init__(self, url):
#         self.app = QApplication(sys.argv)
#         QWebPage.__init__(self)
#         self.loadFinished.connect (self.on_page_load)
#
#     def on_page_load(self):
#         self.app.quit()

# url = 'https://news.google.com/news/?ned=us&gl=US&hl=en'
# client_response = Client(url)

quarter = input('Quarter: ')
year = input('Year: ')
classSubject = input('First letter of your class subject: ')
url = 'https://www.bellevuecollege.edu/classes/' + quarter + year + '?letter=' + classSubject

print(url)

sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
# https://www.bellevuecollege.edu/classes/Spring2018

# for dynamic javascript scraping
# js_test = soup.find('p', class_='jstest')
# print(js_test.text)

# print(soup.title.text) # print the title
# print(soup.find_all('p')) # find all paragraph text with <p> tag
# print(soup.p.text) # print the first paragraph

# print all paragraph without tag
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# get all the url between href tag
# for url in soup.find_all('a'):
#     print(url.get('href'))

# extracting all text from a page
# print(soup.get_text())

# get all data between body tag
# body = soup.body
# for paragraph in body.find_all('p'): # 'p' is the tag name
#     print(paragraph.text)

# retrieve all information from the nav bar
# nav = soup.nav
# for url in nav.find_all('a'):
#     print(url.get('href'))

# find all text between div tag and between body tag
# for div in soup.find_all('div', class_='body'):
#     print(div.text)

# pull data from TABLE
# table = soup.table
# table_rows = table.find_all('tr')
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [i.text for i in td]
#     print(row)

# pull data from table using pandas
# dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header = 0)
# for df in dfs:
#     print(df)
