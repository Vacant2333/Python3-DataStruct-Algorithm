import spider
import networkx as nx
import matplotlib.pyplot as plt

line_data = spider.get_line_data()
# 节点
nodes = {}
# 边
edges = {}
# 上一个站点的名字
last_station_name = ''
for line in line_data.values():
    for station in line:
        # keys存节点(车站)名 value存节点颜色
        nodes[station] = 'green'
        if last_station_name != '' and last_station_name != station:
            # 连接车站,边 颜色为black
            edges[(last_station_name, station)] = 'black'
        last_station_name = station
    last_station_name = ''
# 默认Graph
graph = nx.Graph()
# 添加节点和边到graph中
graph.add_nodes_from(nodes)
graph.add_edges_from(edges.keys())
# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 画布大小8000*4000
plt.figure(figsize=(80, 40))
nx.draw(graph, with_labels=True, node_size=[750], font_size=50, width=6, node_color=nodes.values(), edge_color=edges.values())
plt.show()
