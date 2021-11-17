import requests
from bs4 import BeautifulSoup


# 爬取武汉所有地铁的线路信息

def get_line_data():
    url = 'http://wh.bendibao.com/ditie/linemap.shtml'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    # 线路数据
    line_data = {}
    for line_div in soup.find_all("div", class_="line-list"):
        # heading div 用于获得station name
        heading_div = line_div.findChildren(class_="line-list-heading")
        wrap_div = heading_div[0].findChildren(class_="wrap")
        # 站点名,去掉武汉 和 线路图五个字
        line_name = wrap_div[0].strong.a.contents[0][2:-3]
        # 所有站点
        all_station_div = line_div.findChildren(class_="line-list-station")[0].findChildren(class_="station")
        # 初始化这条线的数据
        line_data[line_name] = []
        # 把站点名全部加到数据中
        for station_div in all_station_div:
            # 根据class为link 拿到所有a标签(站点)
            real_station_div = station_div.findChildren(class_="link")[0]
            line_data[line_name].append(real_station_div.contents[0])
    return line_data
