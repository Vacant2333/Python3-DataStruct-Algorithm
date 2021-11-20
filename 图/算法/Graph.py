# 图,用于实现图类的算法

class UndirectedGraph:
    # 节点 [str]
    nodes = []
    # 边 [[node_1, node_2]]
    edges = []

    # 插入node, node可为str或list[str]
    def insert_node(self, node: str or list):
        if isinstance(node, str):
            # node为str类型
            if self.check_node(node):
                self.nodes.append(node)
        elif isinstance(node, list):
            # node为list类型
            for one_node in node:
                if self.check_node(one_node):
                    self.nodes.append(one_node)
        else:
            # node不是str或list
            raise ValueError("Node must be str or list[str]! node:" + str(node))

    # 插入edge, edge可为list或list[list]
    def insert_edge(self, edge: list):
        pass

    # 检查一个node是否符合 长度大于0且是str类型,不重复
    def check_node(self, node: str):
        # 检查node类型是否为str
        if isinstance(node, str):
            # 检查node长度是否大于0
            if len(node) > 0:
                # 检查node是否重复
                if node not in self.nodes:
                    return True
                else:
                    raise ValueError("Node duplication! node:" + node)
            else:
                raise ValueError("Node length must > 0! node:" + node)
        else:
            raise ValueError("Node must be str! node:" + str(node))

    # 检查一条边是否符合 类型为list且两个节点都存在
    def check_edge(self, edge: list):
        if isinstance(edge, list):
            if len(edge) == 2:
                if self.check_node(edge[0]) and self.check_node(edge[1]):
                    return True
                else:
                    raise ValueError("Edge node error" + str(edge))
            else:
                raise ValueError("Edge length must be 2" + str(edge))
        else:
            raise ValueError("Edge must be list! edge:" + str(edge))


g = UndirectedGraph()
