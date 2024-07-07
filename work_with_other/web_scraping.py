import requests
from bs4 import BeautifulSoup

url = "https://justjoin.it/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headers = soup.find_all("h1")
for header in headers:
    print(header.text)

header2 = soup.find_all("h2")
for header in header2:
    print(header.text)

header3 = soup.find_all("h3")
for header in header3:
    print(header.text)