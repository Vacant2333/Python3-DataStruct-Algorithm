class Node(object):
    # SingleLinkList's node
    def __init__(self, data= None, next_node=None):
        # Data
        self.data = data
        # Next node(node)
        self.next = next_node


class SingleLinkedList:
    def __init__(self):
        self.__head = None
        self.__length = 0

    def is_empty(self) -> bool:
        # Check list is empty
        return False if self.__length else True

    def length(self) -> int:
        return self.__length

    def items(self) -> list:
        # Get all node's data
        re = []
        cur = self.__head
        while cur is not None:
            re.append(cur.data)
            cur = cur.next
        return re

    def add_top(self, data) -> bool:
        tmp = self.__head
        self.__head = Node(data)
        self.__head.next = tmp
        self.__length += 1
        return True

    def add_bottom(self, data) -> bool:
        cur = self.__head
        if self.is_empty():
            self.__head = Node(data)
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)
        self.__length += 1
        return True

    def remove(self, data) -> bool:
        if self.is_empty():
            return False
        if self.length() == 1:
            # There is only the head node
            if self.__head.data == data:
                # Remove the data of head
                self.__head = None
            else:
                return False
        else:
            # There is multiple node
            if self.__head.data == data:
                self.__head = self.__head.next
            else:
                cur = self.__head
                # The last node
                last_cur = None
                while cur.data != data:
                    # Move cursor to the node which should be removed
                    if cur.next is None:
                        return False
                    last_cur = cur
                    cur = cur.next
                last_cur.next = cur.next
        self.__length -= 1
        return True

    def find(self, data) -> bool:
        # Find a node
        cur = self.__head
        while cur is not None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    # Index start from 1 but 0
    def insert(self, index: int, data) -> bool:
        if index == 1:
            self.add_top(data)
            return True
        elif index <= 0 or index > self.length():
            return False
        else:
            cur = self.__head
            now_index = 1
            while now_index == (index - 1):
                # Move cursor to the last of index
                cur = cur.next
                now_index += 1
            tmp = cur.next
            cur.next = Node(data)
            cur.next.next = tmp
        self.__length += 1
        return True

    def clear(self) -> None:
        self.__head = None
        self.__length = 0
