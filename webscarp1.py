from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = input("http://www.dr-chuck.com/page1.htm")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


# retreive all of anchor tags:
tags= soup('a')
for tag in tags:
    print(tag.get('href', None))



# import requests
# url = "https://www.tutorialspoint.com/index.htm"
# req = requests.get(url)
# soup = BeautifulSoup(req.text, "html.parser")
# print(soup.title)