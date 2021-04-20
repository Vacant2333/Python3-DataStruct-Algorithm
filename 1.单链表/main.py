class Node:
    #单链表的节点
    def __init__(self):
        #节点存放的数据
        self.data = None
        #下一个节点
        self.next = None

class SingleLinkList:
    #单链表
    def __init__(self):
        #初始化,head节点存放链表长度
        self.head = Node()
        self.head.data = 0