from bs4 import BeautifulSoup
import requests
import module

url = "https://www.susu.ru/ru/lessons"
response = requests.get(url)
bs = BeautifulSoup(response.text, "lxml")
temp = bs.find("ul", "views-summary")
content = [i for i in temp if
           str(type(i)) != "<class 'bs4.element.NavigableString'>"]

urls = [str(i).split('\"')[1] for i in content]
audiences = []

for i in range(len(urls)):
    temp = module.request_groups(urls[i])
    group_urls = module.request_transform(temp)

    for j in group_urls:
        audiences.append(module.captured_audiences(j))

result = set()
for i in audiences:
    for j in i:
        result.add(j)

with open("result.txt", "w+") as file:
    file.write(str(result))
