import networkx as nx
import matplotlib.pyplot as plt

# 绘制无向图
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
graph.add_nodes_from(nodes.keys())
graph.add_weighted_edges_from(edges)

edge_label = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, nx.spiral_layout(graph), edge_labels=edge_label)


nx.draw(graph, with_labels=True, node_color=nodes.values(), font_size=15, pos=nx.spiral_layout(graph))
plt.show()


print(graph.edges(data=True))
print(graph.nodes)
