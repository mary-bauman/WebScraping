from bs4 import BeautifulSoup
import requests

url = "https://www.recreation.gov/camping/campgrounds/232507"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.text)
#error