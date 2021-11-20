import networkx as nx
import matplotlib.pyplot as plt

nodes = {
    'start': 'yellow',
    'a': 'green',
    'b': 'green',
    'c': 'green',
    'end': 'yellow'
}

edges = [
    ('start', 'a', 1),
    ('start', 'b', 5),
    ('a', 'b', 4),
    ('a', 'c', 2),
    ('b', 'end', 3),
    ('b', 'c', 4)
]

graph = nx.Graph()
# Add nodes to graph
graph.add_nodes_from(nodes)
# Add edges with weight to graph
graph.add_weighted_edges_from(edges)
# Graph type
pos = nx.spiral_layout(graph)
# Get weight's data and draw labels
edge_label = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_label)
nx.draw(graph, with_labels=True, node_color=nodes.values(), pos=pos)
plt.show()
