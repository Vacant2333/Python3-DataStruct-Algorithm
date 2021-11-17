import spider

line_data = spider.get_line_data()

# 节点
nodes = {}
edges = {}
last_station_name = ''

for (line_name, line) in line_data.items():
    for station in line:
        nodes[station] = {
            'color': 'green'
        }
        if last_station_name != '' and last_station_name != station:
            edges[(last_station_name, station)] = {
                'color': 'black'
            }
        last_station_name = station

print(nodes)
print(edges)
