class BreadthFirstSearch:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.check_list = []

    def get_node_neighbor(self, node: str) -> list:
        neighbor = []
        for edge in self.edges:
            if node in edge:
                edge.remove(node)
                neighbor.append(edge.pop())
        return neighbor

    def breadth_first_search(self, nodes: list, edges: list, start: str, end: str) -> bool:
        self.nodes = nodes
        self.edges = edges
        self.check_list = [start]
        pass
