from bs4 import BeautifulSoup
import requests
html_doc = """<html><head><title>The Dormouse's Story</title></head>
<body>
<p class="title"><b>The Little Guy's Story</b></p>
<a href="https://www.google.com">Google</a>
"""

soup = BeautifulSoup(html_doc, "html.parser")

# print(soup.find(href="https://www.google.com").text)

print("\n", soup.title.string)
print("\n", soup.find(class_="title").b.string)
# print(soup.p.b.string, "\n")
# print(soup.prettify())




