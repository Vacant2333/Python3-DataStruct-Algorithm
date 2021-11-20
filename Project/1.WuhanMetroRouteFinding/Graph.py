import Spider
import networkx as nx
import matplotlib.pyplot as plt

line_data = Spider.get_line_data()
nodes = {}
edges = {}
# Last station
last_station_name = ''
for line in line_data.values():
    for station in line:
        # Key: station name, value: node color
        nodes[station] = 'green'
        if last_station_name != '' and last_station_name != station:
            # Save edge(link station)
            edges[(last_station_name, station)] = 'black'
        last_station_name = station
    last_station_name = ''
graph = nx.Graph()
# Add nodes and graph to graph
graph.add_nodes_from(nodes)
graph.add_edges_from(edges.keys())
# For chinese
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# Canvas size: 8000*4000
plt.figure(figsize=(80, 40))
nx.draw(graph, with_labels=True, node_size=[750], font_size=50, width=6, node_color=nodes.values(), edge_color=edges.values())
plt.show()
