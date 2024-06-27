from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Competitive_programming'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
sectionHeads = soup.find_all('span', attrs={'class': 'mw-headline'})
for s in sectionHeads:
    print(s.text)
# print(sectionHeads);