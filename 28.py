import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com"
r = requests.get(url)
print(r.status_code)
a = BeautifulSoup(r.text,"html.parser")
b = a.find_all("div",class_ = "quote")
for k in b:
    ming = k.find("span",class_ = "text").text
    zuozhe = k.find("small",class_ = "author").text
    biao = k.find_all("a",class_ = "tag")
    wenben = [c.text for c in biao]
    print(ming)
    print(zuozhe)
    print(wenben)