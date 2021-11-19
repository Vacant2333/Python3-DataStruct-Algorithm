# 图,用于实现图类的算法

class Graph:
    # 节点 [str]
    nodes = []
    # 边 [[node_1, node_2]]
    edges = []

    # 插入node, node可为str或list[str]
    def insert_node(self, node: str or list):
        if isinstance(node, str):
            # node为str类型
            if len(node) >= 1:
                # 检查node是否重复
                if not self.exists_node(node):
                    self.nodes.append(node)
                else:
                    raise ValueError("node duplication : " + str(node))
            else:
                raise ValueError("node length must >= 1")
        elif isinstance(node, list):
            # node为list类型
            for one_node in node:
                if isinstance(one_node, str):
                    # 检查node是否重复
                    if not self.exists_node(one_node):
                        self.nodes.append(one_node)
                    else:
                        raise ValueError("node duplication : " + str(one_node))
                else:
                    raise ValueError("node must be str or list[str]")
        else:
            # node类型不为str或list
            raise ValueError("node must be str or list[str]")

    # 检查node是否已存在
    def exists_node(self, node: str):
        return node in self.nodes


g = Graph()
g.insert_node(['1', '2', '3', ''])
g.insert_node('1')
print(g.nodes)
