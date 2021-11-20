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
            self.check_node(node)
            self.nodes.append(node)
        elif isinstance(node, list):
            # node为list类型
            for one_node in node:
                self.check_node(one_node)
                self.nodes.append(one_node)
        else:
            # node不是str或list
            raise ValueError("Node must be str or list[str]! node:" + str(node))

    # 插入edge, edge可为list或list[list]
    def insert_edge(self, edge: list):
        # 检查edge参数类型
        if isinstance(edge, list):
            # 判断是单个边还是多个
            if isinstance(edge[0], list):
                # 多个边
                for one_edge in edge:
                    self.check_edge(one_edge)
                    self.edges.append(one_edge)
            else:
                # 单条边
                self.check_edge(edge)
        else:
            raise ValueError("Edge must be list! edge:" + str(edge))

    # 检查一个node是否符合 长度大于0且是str类型,不重复
    def check_node(self, node: str):
        # 检查类型是否为str
        if not isinstance(node, str):
            raise ValueError("Node must be str! node:" + str(node))
        # 检查长度是否大于0
        if len(node) == 0:
            raise ValueError("Node length must > 0! node:" + node)
        # 检查是否重复
        if node in self.nodes:
            raise ValueError("Node duplication! node:" + node)

    # 检查一条边是否符合 类型为list且两个节点都存在
    def check_edge(self, edge: list):
        # 检查类型
        if not isinstance(edge, list):
            raise ValueError("Edge must be list! edge:" + str(edge))
        # 检查长度
        if len(edge) != 2:
            raise ValueError("Edge length must be 2" + str(edge))
        # 检查节点
        self.check_node(edge[0])
        self.check_node(edge[1])


g = UndirectedGraph()
