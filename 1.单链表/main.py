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
        #初始化
        self._head = None
        self._length = 0

    def is_empty(self) -> bool:
        #判断链表是否为空
        return False if (self.length()) else True

    def length(self) -> int:
        #获取链表长度
        return self._length

    def items(self) -> list:
        #获得链表所有数据
        re = []
        cur = self._head
        while(cur != None):
            re.append(cur.data)
            cur = cur.next
        return re

    def add_top(self, data) -> bool:
        #向链表头部添加节点
        tmp = self._head
        self._head = Node(data)
        self._head.next = tmp
        self._length += 1
        return True

    def add_bottom(self, data) -> bool:
        #向链表尾部添加节点
        cur = self._head
        if(self.length() == 0):
            #判断是否是空链表
            self._head = Node(data)
        else:
            while(cur.next != None):
                cur = cur.next
            cur.next = Node(data)
        self._length += 1
        return True

    def remove(self, data) -> bool:
        #删除节点
        if(self.length() <= 1):
            #判断链表长度
            if(self.length() == 0):
                #判断是否是空链表
                return False
            else:
                if(self._head.data == data):
                    #判断唯一元素是否是data
                    self.head = None
                else:
                    return False
        else:
            cur = self._head
            last_cur = None
            #last_cur存放上一个节点
            while(cur.data != data):
                #游标移到需要删除的节点
                if(cur.next == None):
                    return False
                last_cur = cur
                cur = cur.next
            last_cur.next = cur.next
        self._length -= 1
        return True

    def find(self, data) -> bool:
        #判断节点是否存在
        cur = self._head
        while(cur != None):
            if(cur.data == data):
                return True
            cur = cur.next
        return False

    def insert(self, index, data) -> bool:
        #插入节点
        if(index == 1):
            self.add_top(data)
        elif(index == self.length()):
            self.add_bottom(data)
        elif(index <= 0 or index > self.length()):
            return False
        else:
            cur = self._head
            now_index = 1
            while(cur.next != None):

                cur = cur.next


        return