import requests
from bs4 import BeautifulSoup


def request_groups(url):
    response = requests.get(f'https://www.susu.ru{url}')
    bs = BeautifulSoup(response.text, 'lxml')
    return bs.find_all("span", "field-content")


def request_transform(self):
    for i in self:
        for j in i:
            if str(type(j)) == "<class 'bs4.element.NavigableString'>":
                i.remove(j)

    urls_array = []
    for i in self:
        for j in i:
            urls_array.append(str(j).split('\"')[1])
    return urls_array


def captured_audiences(url):
    response = requests.get(f"https://www.susu.ru{url}")
    bs = BeautifulSoup(response.text, 'lxml')
    temp = bs.find_all("td")
    audiences = set()
    for i in temp:
        j = i.text.split()
        if '/' in str(j):
            audiences.add(j[0])
    return audiences
