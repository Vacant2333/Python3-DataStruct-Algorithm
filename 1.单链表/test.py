from main import SingleLinkList

sll = SingleLinkList()

sll.add_top(1)
sll.add_top(2)
#sll.add_top(3)
print(sll.head.next.next.data)
print(sll.head.data)