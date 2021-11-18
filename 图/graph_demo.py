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

# 新graph
graph = nx.Graph()
# 把node和带权重的edge添加到graph
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)
# position
pos = nx.spiral_layout(graph)
# 取weight数据并设置edge label
edge_label = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_label)
nx.draw(graph, with_labels=True, node_color=nodes.values(), pos=pos)
plt.show()
