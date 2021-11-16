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

# new a graph
graph = nx.Graph()
# add nodes and edges with weight
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)

pos = nx.spiral_layout(graph)
edge_label = nx.get_edge_attributes(graph, 'weight')

nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_label)
nx.draw(graph, with_labels=True, node_color=nodes.values(), pos=pos)
plt.show()


print(graph.edges(data=True))
print(graph.nodes)
