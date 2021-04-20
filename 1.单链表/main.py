class Node:
    #单链表的节点
    def __init__(self, data):
        #节点存放的数据
        self.data = data
        #下一个节点
        self.next = None

class SingleLinkList:
    #单链表
    def __init__(self):
        #初始化,head节点存放链表长度
        self.head = Node(0)

    def is_empty(self) -> bool:
        #判断链表是否为空
        return False if self.head.next else True

    def length(self) -> int:
        #获取链表长度
        return self.head.data

    def has_key(self, key):
        #查询是否有此节点
        return True if key >= self.length() else False

    def add_top(self, data) -> bool:
        #向链表头部添加节点
        tmp = self.head.next
        self.head.next = Node(data)
        self.head.next.next = tmp
        return True

    def add_bottom(self, data) -> bool:
        #向链表尾部添加节点
        self.head.data += 1
        if(self.head.next == None):
            self.head.next = Node(data)
        else:
            cur = self.head.next
            while(cur.next != None):
                cur = cur.next
            cur.next = Node(data)
        return True