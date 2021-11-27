import requests
from bs4 import BeautifulSoup


def get_line_data() -> dict:
    url = 'http://wh.bendibao.com/ditie/linemap.shtml'
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    # Metro line data
    line_data = {}
    for line_div in soup.find_all("div", class_="line-list"):
        # Heading div
        heading_div = line_div.findChildren(class_="line-list-heading")
        wrap_div = heading_div[0].findChildren(class_="wrap")
        # Divide station name
        line_name = wrap_div[0].strong.a.contents[0][2:-3]
        all_station_div = line_div.findChildren(class_="line-list-station")[0].findChildren(class_="station")
        # Init the line
        line_data[line_name] = []
        # Add all station name to the line
        for station_div in all_station_div:
            # Get a label by condition (class = "link")
            real_station_div = station_div.findChildren(class_="link")[0]
            line_data[line_name].append(real_station_div.contents[0])
    return line_data
