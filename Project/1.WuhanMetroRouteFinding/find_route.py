from Graph.DataStruct.UndirectedGraph import UndirectedGraph
from Graph.Algorithm.BreadthFirstSearch import BreadthFirstSearch2
import line_data_spider

line_data = line_data_spider.get_line_data()
nodes = []
edges = []
# Last station
last_station_name = ''
for line in line_data.values():
    for station in line:
        # Key: station name, value: node color
        nodes.append(station)
        if last_station_name != '' and last_station_name != station:
            # Save edge(link station)
            edges.append([station, last_station_name])
        last_station_name = station
    last_station_name = ''

# Remove duplicate
nodes = list(set(nodes))
# Dirty data
edges.remove(['中南路', '洪山广场'])

graph = UndirectedGraph()
graph.add_node(nodes)
graph.add_edge(edges)

# Get route
print(BreadthFirstSearch2().run(graph, '天河机场', '佛祖岭'))
print(BreadthFirstSearch2().run(graph, '石桥', '中山公园'))
