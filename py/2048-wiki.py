from bs4 import BeautifulSoup
import requests

response = requests.get('https://en.wikipedia.org/wiki/2048_(video_game)')
soup = BeautifulSoup(response.text, 'html.parser')

#text of top level heading (h1)


#how many second level headings (h2)


#extract href of first link on page