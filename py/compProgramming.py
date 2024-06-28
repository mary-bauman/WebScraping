from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Competitive_programming'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

sectionHeads = soup.find_all('span', attrs={'class': 'mw-headline'})
print("\nSection Heads")
for sectionHead in sectionHeads: print(sectionHead.text)

titles = soup.find_all(['title', 'h1', 'h2'])
print("\nTitles")
for t in titles: print(t.text)