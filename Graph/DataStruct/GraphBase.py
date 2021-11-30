class GraphBase:
    # Nodes: [str, ...]
    nodes = []
    # Edges: [[node_1, node_2], ...]
    # Edge with weight: [[node_1, node_2, weight], ...]
    edges = []

    def get_nodes(self) -> list[int]:
        return self.nodes

    def get_edges(self) -> list[list[str, str]] or list[list[str, str, int]]:
        return self.edges

    def get_node_neighbor(self, node: str, directed: bool = False) -> list[str]:
        neighbor = []
        if directed:
            # Directed graph
            # TODO: get neighbor
            pass
        else:
            for edge in self.edges:
                if node in edge:
                    neighbor.append(edge[1] if edge.index(node) == 0 else edge[0])
        return neighbor
