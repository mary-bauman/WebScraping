from bs4 import BeautifulSoup
import requests

url = 'https://drewgoodenshop.com/?utm_source=youtube&utm_medium=product_shelf'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

#aria-label="Hey Guy Moving and Storage Mint Green Tee" 
heyGuyMint = (soup.find_all('a', attrs={'aria-label': 'Hey Guy Moving and Storage Mint Green Tee'}))
newHeyGuyMint = []
for item in heyGuyMint:
    item = item.text
    item = item.strip()
    item = item.replace("\n", "")
    item = item.replace("    ", "")
    if item:
        newHeyGuyMint.append(item)
heyGuyMint = newHeyGuyMint
for item in heyGuyMint: print(item)
