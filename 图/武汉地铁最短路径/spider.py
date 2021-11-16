import requests
from bs4 import BeautifulSoup

url = 'http://wh.bendibao.com/ditie/linemap.shtml'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')

# 线路数据(所有站点)
line_data = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '6': [],
    '7': [],
    '8': [],
    '阳逻': [],
    '11': []
}

for station_list in soup.find_all("div", class_="line-list-station"):
    print(len(station_list))



