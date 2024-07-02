from bs4 import BeautifulSoup
import requests

response = requests.get('https://en.wikipedia.org/wiki/2048_(video_game)')
soup = BeautifulSoup(response.text, 'html.parser')

#text of top level heading (h1)
h1 = soup.find('h1')
print(h1.text)

#how many second level headings (h2)
h2s = soup.find_all('h2')
print(len(h2s))


#extract href of first link on page
firstLink = soup.find('a')['href']
print(firstLink)
