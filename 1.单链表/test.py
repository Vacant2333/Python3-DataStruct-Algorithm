from main import SingleLinkList

sll = SingleLinkList()

sll.add_bottom(1)
sll.add_bottom(2)
sll.add_bottom(3)
sll.remove(2)

print(sll.items())
print(sll.length())