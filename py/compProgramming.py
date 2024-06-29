from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Competitive_programming'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

sectionHeads = soup.find_all('span', attrs={'class': 'mw-headline'})
# print("\nSection Heads")
# for sectionHead in sectionHeads: print(sectionHead.text)

#mw-default-size
mw = soup.find(class_="mw-default-size")
# print(mw)
# print(mw.text)
# print(mw.contents)
# print(mw.attrs)
# print(f"for all {len(mw)} children")
# for child in mw.children:
#     print("\nchild")
#     print(child)
# descendants = list(mw.descendants)
# print(f"for all {len(descendants)} descendants")
# for d in descendants:
#     print(d, "\n")
# parents = list(mw.parents)
# print(f"for all {len(parents)} parents:\n")
# for p in parents: print(p, "\n")



# titles = soup.find_all(['title', 'h1', 'h2'])
# print("\nTitles")
# for t in titles: print(t.text)
# firstTitle = soup.find(['title', 'h1', 'h2'])
# nextSibling = firstTitle.next_sibling
# #note that floating whitespace is considered a sibling
# print(f"{firstTitle.text} and {nextSibling.text} are siblings")
# nextSibling = nextSibling.next_sibling
# print(f"{nextSibling.text} is the next sibling")