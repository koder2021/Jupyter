import requests
from bs4 import BeautifulSoup

url = "https://www.wildberries.ru/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup)

lst = soup.find_all(class_ ='menu-burger__main-list-link')

for item in lst:
    print(item)
    
def clean_item(my_item):
    position1 = my_item.find('>') + 1
    position2 = my_item.find('</')
    return my_item[position1:position2]
    
print("")

for item in lst:
    print(clean_item(str(item)))
