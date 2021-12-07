from DataStruct.Graph.UndirectedGraph import UndirectedGraph


class DepthFirstSearch:
    def __init__(self):
        self.check_stack = []
        self.nodes = []
        self.edges = []
        self.checked_node = []

    def filter_checked_node(self, nodes: list[str]) -> list[str]:
        for checked_node in self.checked_node:
            if checked_node in nodes:
                nodes.remove(checked_node)
        return nodes

    def run(self, graph: UndirectedGraph, start: str, end: str) -> bool:
        self.nodes = graph.get_nodes()
        self.edges = graph.get_edges()
        self.checked_node = [start]
        self.check_stack = [start]
        while len(self.check_stack) > 0:
            deepest_node = self.check_stack[-1]
            if deepest_node is not end:
                check_node_neighbor = self.filter_checked_node(graph.get_node_neighbor(deepest_node))
                print("Neighbor node:{}  ".format(check_node_neighbor), end='')
                if len(check_node_neighbor) > 0:
                    # Get the deepest_node's neighbor node,and choose one add to stack
                    next_node = check_node_neighbor[0]
                    # Add next_node to check_node to avoid loops
                    self.checked_node.append(next_node)
                    self.check_stack.append(next_node)
                    print("Next node:{}".format(next_node))
                else:
                    # Backtracking because there are no child nodes and its not the end node
                    pop_node = self.check_stack.pop()
                    print("Backtrack to node:{}".format(pop_node))
            else:
                # It's end node
                return True
        return False
