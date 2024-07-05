from bs4 import BeautifulSoup
import requests

url = 'http://www.recreation.gov/camping/campsites/5751'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.text)
#error