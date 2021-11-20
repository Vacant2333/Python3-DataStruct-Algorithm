import networkx as nx
import time
import random

# timer(ms)
start_time = int(round(time.time() * 1000))

# Ternary operator
a = 1
b = 2
True if a == b else False

# random number [0, 9]
print(random.randint(0, 9))

# NetworkX shows edge weight on label
graph = nx.Graph()
# pos means the type of graph
pos = nx.spiral_layout(graph)
edge_label = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_label)
