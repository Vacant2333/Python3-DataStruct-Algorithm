from main import SingleLinkList

sll = SingleLinkList()

sll.add_bottom(1)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.add_bottom(2)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.add_bottom(3)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.add_bottom(4)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.add_bottom(6)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.insert(5, 5)
print("{}  length:{}".format(sll.items(), sll.length()))