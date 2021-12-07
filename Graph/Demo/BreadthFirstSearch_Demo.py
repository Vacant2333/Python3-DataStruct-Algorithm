from Graph.Algorithm.BreadthFirstSearch import BreadthFirstSearch1, BreadthFirstSearch2
from DataStruct.Graph.UndirectedGraph import UndirectedGraph

graph = UndirectedGraph()

# Graph image on README.md
nodes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
edges = [['0', '1'], ['0', '2'], ['0', '6'], ['6', '4'], ['3', '4'], ['4', '5'], ['3', '5'], ['0', '5'], ['7', '8'], ['9', '10'], ['11', '12'], ['9', '11'], ['9', '12']]

graph.add_node(nodes)
graph.add_edge(edges)

# Version 1
print(BreadthFirstSearch1().run(graph, '0', '3'))
print(BreadthFirstSearch1().run(graph, '0', '8'))

# Version 2,return with the shortest route
print(BreadthFirstSearch2().run(graph, '10', '12'))
print(BreadthFirstSearch2().run(graph, '0', '7'))
