# 计时 毫秒单位
import time
start_time = int(round(time.time() * 1000))

#三元运算符
666 if a == b else 111

#随机数 [0, 9]
import random
print(random.randint(0,9))

#networkx draw权重
pos = nx.spiral_layout(graph)
edge_label = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_label)