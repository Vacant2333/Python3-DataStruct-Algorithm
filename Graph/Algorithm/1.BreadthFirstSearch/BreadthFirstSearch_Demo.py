import BreadthFirstSearch
bfs = BreadthFirstSearch.BreadthFirstSearch()
nodes = ['1','2','3']
edges = [['1','2'],['2','3']]
print(bfs.breadth_first_search(nodes,edges,'1','3'))
