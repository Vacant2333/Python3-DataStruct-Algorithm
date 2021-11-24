import time
from DataStruct import SingleLinkedList

sll = SingleLinkedList.SingleLinkedList()

# Check SingleLinkedList methods
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
sll.add_top(0)
print("{}  length:{}".format(sll.items(), sll.length()))
print("find 5:{}  find 7:{}  is_empty:{}".format(sll.find(5), sll.find(7), sll.is_empty()))
sll.remove(1)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.remove(2)
print("{}  length:{}".format(sll.items(), sll.length()))
sll.remove(3)
print("{}  length:{}".format(sll.items(), sll.length()))

num = 10000

# Insert speed test
print("Insert {} data in list and SingleLinkedList".format(num))
start_time = int(round(time.time() * 1000))

for x in range(num):
    sll.insert(int(x/2), (x * 125) % 6)
print("SingleLinkedList:{}ms".format(int(round(time.time() * 1000)) - start_time))

start_time = int(round(time.time() * 1000))
test = [0, 4, 5, 9]
for y in range(num):
    test.insert(int(y/2), (y * 125) % 6)
print("List::{}ms".format(int(round(time.time() * 1000)) - start_time))
