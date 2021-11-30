from Sorting.DataStruct.SingleLinkedList import SingleLinkedList

sll = SingleLinkedList()

# Check SingleLinkedList methods
sll.add_bottom(1)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.add_bottom(2)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.add_bottom(4)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.insert(3, 3)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.add_top(0)
print("{}  length:{}".format(sll.items(), sll.length()))
print("find 5:{}  find 7:{}  is_empty:{}".format(sll.find(3), sll.find(7), sll.is_empty()))
sll.remove(1)
print("{}  length:{}".format(sll.items(), sll.length()))
