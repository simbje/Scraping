

'''
Scraping in python test
'''

# prerequisites
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd
#

url = "https://www.finn.no/realestate/homes/search.html?q=oslo&sort=PUBLISHED_DESC"

result = requests.get(url)
doc = soup(result.text, "html.parser")
print(doc.prettify())


## data some eg vil ha

adresse = []
beskrivelse = []
pris= []
total_pris = []

bolig_data = soup.findAll('div', attrs= {'class':'p-16 grid f-grid sm:grid-cols-2'})

print(bolig_data)






