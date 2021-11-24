class BreadthFirstSearch1:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.check_list = []
        self.checked_node = []

    def get_node_neighbor(self, node: str) -> list:
        neighbor = []
        for edge in self.edges:
            if node in edge:
                neighbor.append(edge[1] if edge.index(node) == 0 else edge[0])
        return neighbor

    def filter_checked_node(self, nodes: list) -> list:
        for checked_node in self.checked_node:
            if checked_node in nodes:
                nodes.remove(checked_node)
        return nodes

    def run(self, nodes: list, edges: list, start: str, end: str) -> bool:
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


# Return with the shortest route
class BreadthFirstSearch2:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.check_list = []
        self.checked_node = []
        # Structure: nodes_father[son_node] = father_node
        self.nodes_father = {}
        # Start cost 0, each step cost 1
        self.node_cost = {}

    def get_node_neighbor(self, node: str) -> list:
        neighbor = []
        for edge in self.edges:
            if node in edge:
                neighbor.append(edge[1] if edge.index(node) == 0 else edge[0])
        return neighbor

    def filter_checked_node(self, nodes: list) -> list:
        for checked_node in self.checked_node:
            if checked_node in nodes:
                nodes.remove(checked_node)
        return nodes

    def get_node_route(self, node: str) -> list:
        route = [node]
        while True:
            last_node = route[-1]
            if last_node in self.nodes_father.keys():
                route.append(self.nodes_father[last_node])
            else:
                break
        return route

    # Get a node cost(start cost is 0)
    def get_node_cost(self, node: str) -> int:
        if node in self.node_cost.keys():
            return self.node_cost[node]
        else:
            # Return infinite
            return float('inf')

    # Save a node's father node and update cost
    def save_father_node(self, father_node: str, son_node: str) -> None:
        if son_node in self.nodes_father.keys():
            if self.get_node_cost(son_node) > self.get_node_cost(father_node) + 1:
                self.node_cost[son_node] = self.get_node_cost(father_node) + 1
                self.nodes_father[son_node] = father_node
        else:
            self.node_cost[son_node] = self.get_node_cost(father_node) + 1
            self.nodes_father[son_node] = father_node

    def run(self, nodes: list, edges: list, start: str, end: str) -> bool or list:
        self.nodes = nodes
        self.edges = edges
        self.check_list = [start]
        self.node_cost[start] = 0
        for check_node in self.check_list:
            if check_node != end:
                # Get Node neighbor and filter node which had checked
                node_neighbor = self.filter_checked_node(self.get_node_neighbor(check_node))
                for neighbor_node in node_neighbor:
                    self.save_father_node(check_node, neighbor_node)
                # Add neighbor node to check_list to search all node
                self.check_list += node_neighbor
                self.checked_node.append(check_node)
            else:
                # Its end node and reverse the route
                return self.get_node_route(end)[::-1]
        # Cant find end node
        return False
