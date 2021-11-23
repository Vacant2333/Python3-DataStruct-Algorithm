class BreadthFirstSearch:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.check_list = []
        self.checked_node = []

    def get_node_neighbor(self, node: str) -> list:
        neighbor = []
        for edge in self.edges:
            if node in edge:
                edge.remove(node)
                neighbor.append(edge.pop())
        return neighbor

    def filter_checked_node(self, nodes: list) -> list:
        for checked_node in self.checked_node:
            if checked_node in nodes:
                nodes.remove(checked_node)
        return nodes

    def breadth_first_search(self, nodes: list, edges: list, start: str, end: str) -> bool:
        self.nodes = nodes
        self.edges = edges
        self.check_list = [start]
        for check_node in self.check_list:
            if check_node != end:
                # Get Node neighbor and filter node which had checked
                node_neighbor = self.filter_checked_node(self.get_node_neighbor(check_node))
                # Add neighbor node to check_list to search all node
                self.check_list += node_neighbor
                self.checked_node.append(check_node)
            else:
                # Its end node
                return True
        # Cant find end node
        return False

