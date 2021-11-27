from Graph.DataStruct.UndirectedGraph import UndirectedGraph


# Version 1,mere search the route if can arrive the end node
class BreadthFirstSearch1:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.check_queue = []
        self.checked_node = []

    def filter_checked_node(self, nodes: list[str]) -> list[str]:
        for checked_node in self.checked_node:
            if checked_node in nodes:
                nodes.remove(checked_node)
        return nodes

    def run(self, graph: UndirectedGraph, start: str, end: str) -> bool:
        self.nodes = graph.get_nodes()
        self.edges = graph.get_edges()
        self.check_queue = [start]
        for check_node in self.check_queue:
            if check_node != end:
                # Get Node neighbor and filter node which had checked
                check_node_neighbor = self.filter_checked_node(graph.get_node_neighbor(check_node))
                for neighbor in check_node_neighbor:
                    self.checked_node.append(neighbor)
                # Add neighbor node to check_queue to search all node
                self.check_queue += check_node_neighbor
                self.checked_node.append(check_node)
            else:
                # Its end node
                # print(self.check_queue)
                return True
        # Cant find end node
        return False


# Version 2,return with the shortest route if can arrive the end node
class BreadthFirstSearch2:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.check_queue = []
        self.checked_node = []
        # Structure: nodes_father[son_node] = father_node
        self.nodes_father = {}
        # Start cost 0, each step cost 1
        self.node_cost = {}

    def filter_checked_node(self, nodes: list[str]) -> list[str]:
        for checked_node in self.checked_node:
            if checked_node in nodes:
                nodes.remove(checked_node)
        return nodes

    def get_node_route(self, node: str) -> list[str]:
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

    def run(self, graph: UndirectedGraph, start: str, end: str) -> bool or list[str]:
        self.nodes = graph.get_nodes()
        self.edges = graph.get_edges()
        self.check_queue = [start]
        self.node_cost[start] = 0
        for check_node in self.check_queue:
            if check_node != end:
                # Get Node neighbor and filter node which had checked
                check_node_neighbor = self.filter_checked_node(graph.get_node_neighbor(check_node))
                for neighbor in check_node_neighbor:
                    self.save_father_node(check_node, neighbor)
                    self.checked_node.append(neighbor)
                # Add neighbor node to check_queue to search all node
                self.check_queue += check_node_neighbor
                self.checked_node.append(check_node)
                # print(check_node)
            else:
                # Its end node and reverse the route
                # print(self.check_queue)
                return self.get_node_route(end)[::-1]
        # Cant find end node
        return False
