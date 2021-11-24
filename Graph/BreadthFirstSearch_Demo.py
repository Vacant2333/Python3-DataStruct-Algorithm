from Algorithm import BreadthFirstSearch


nodes = ['1', '2', '3']
edges = [['1', '2'], ['2', '3']]
print(BreadthFirstSearch.BreadthFirstSearch().breadth_first_search(nodes, edges, '1', '3'))
