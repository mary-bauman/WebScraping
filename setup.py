from bs4 import BeautifulSoup
import requests
html_doc = """<html><head><title>The Dormouse's Story</title></head>
<body>
<p class="title"><b>The Little Guy's Story</b></p>
"""

soup = BeautifulSoup(html_doc, "html.parser")
print("\n", soup.title.string)
print(soup.p.b.string, "\n")
print(soup.prettify())





response = requests.get('https://www.google.com')
# print(response.text)