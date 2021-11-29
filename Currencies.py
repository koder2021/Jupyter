import requests
import xmltodict

url = "http://www.cbr.ru/scripts/XML_daily.asp"
# ~ url = "http://parsing.tw1.su/XML_daily.asp"
response = requests.get(url)
data = xmltodict.parse(response.content)
print(data)

my_array = []
for item in data['ValCurs']['Valute']:
    # ~ my_set = [item['CharCode'], item['Name'], item['Value']];
    my_set = [item['Name'], item['Nominal']];
    my_array.append(my_set)
    print(my_set)
    # ~ print(my_array)


