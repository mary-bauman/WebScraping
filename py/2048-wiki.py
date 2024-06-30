from bs4 import BeautifulSoup
import requests

response = requests.get('https://en.wikipedia.org/wiki/2048_(video_game)')
soup = BeautifulSoup(response.text, 'html.parser')
