

'''
Scraping in python test
'''

# prerequisites
from bs4 import BeautifulSoup as bs
import requests
#

url = "https://www.finn.no/realestate/homes/search.html?q=oslo&sort=PUBLISHED_DESC"

result = requests.get(url)
doc = bs(result.text, "html.parser")
print(doc.prettify())
