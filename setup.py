from bs4 import BeautifulSoup
import requests
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
"""

soup = BeautifulSoup(html_doc)
print(soup.title)