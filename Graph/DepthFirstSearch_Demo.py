from Graph.Algorithm.DepthFirstSearch import DepthFirstSearch
from Graph.DataStruct.UndirectedGraph import UndirectedGraph

graph = UndirectedGraph()

# Graph image on README.md
nodes = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
edges = [['1', '2'], ['2', '3'], ['2', '5'], ['3', '4'], ['5', '4'], ['1', '8'], ['8', '6'], ['8', '9'], ['4', '6'], ['6', '7']]

graph.add_node(nodes)
graph.add_edge(edges)

print(DepthFirstSearch().run(graph, '1', '7'))
print(DepthFirstSearch().run(graph, '1', '10'))
