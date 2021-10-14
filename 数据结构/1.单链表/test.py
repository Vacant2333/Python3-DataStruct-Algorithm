import time
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
print("插入{}条数据性能对比(list)".format(num))
start_time = int(round(time.time() * 1000))
sll.add_top(6666)
for x in range(num):
    sll.insert(int(x/2), (x * 125) % 6)
print("单链表耗时:{}毫秒".format(int(round(time.time() * 1000)) - start_time))
start_time = int(round(time.time() * 1000))
test = [0, 4, 5, 9]
for y in range(num):
    test.insert(int(y/2), (y * 125) % 6)
print("列表耗时:{}毫秒".format(int(round(time.time() * 1000)) - start_time))
