class BreadthFirstSearch:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def get_node_neighbor(self, node: str) -> list:
        neighbor = []
        for edge in self.edges:
            if node in edge:
                edge.remove(node)
                neighbor.append(edge.pop())
        return neighbor
