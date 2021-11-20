class Node:
    # SingleLinkList's node
    def __init__(self, data):
        # Data
        self.data = data
        # Next node(node)
        self.next = None


class SingleLinkList:
    def __init__(self):
        self._head = None
        self._length = 0

    def is_empty(self) -> bool:
        # Check list is empty
        return False if self._length else True

    def length(self) -> int:
        return self._length

    def items(self) -> list:
        # Get all node's data
        re = []
        cur = self._head
        while cur is not None:
            re.append(cur.data)
            cur = cur.next
        return re

    def add_top(self, data) -> bool:
        tmp = self._head
        self._head = Node(data)
        self._head.next = tmp
        self._length += 1
        return True

    def add_bottom(self, data) -> bool:
        cur = self._head
        if self.is_empty():
            self._head = Node(data)
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)
        self._length += 1
        return True

    def remove(self, data) -> bool:
        if self._length <= 1:
            if self.is_empty():
                return False
            else:
                if self._head.data == data:
                    # Remove the data of head
                    self._head = None
                else:
                    return False
        else:
            cur = self._head
            # The last node
            last_cur = None
            while cur.data != data:
                # Move cursor to the node which should be removed
                if cur.next is None:
                    return False
                last_cur = cur
                cur = cur.next
            last_cur.next = cur.next
        self._length -= 1
        return True

    def find(self, data) -> bool:
        # Find a node
        cur = self._head
        while cur is not None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def insert(self, index, data) -> bool:
        if index == 1:
            self.add_top(data)
            return True
        elif index <= 0 or index > self.length():
            return False
        else:
            cur = self._head
            now_index = 1
            while int(now_index) != (index - 1):
                # Move cursor to the last of index
                cur = cur.next
                now_index += 1
            tmp = cur.next
            cur.next = Node(data)
            cur.next.next = tmp
        self._length += 1
        return True

    def clear(self) -> bool:
        self._head = None
        self._length = 0
        return True
