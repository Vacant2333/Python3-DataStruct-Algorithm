from DataStruct.Queue import Queue

queue = Queue()

queue.put(1)
queue.put(2)
queue.put(3)
print("Values: {}".format(queue.values()))
print("Pop: {}".format(queue.get()))
queue.put(4)
print("Get top:{}".format(queue.get_top()))

print(queue.get_length())
print(queue.values())
print(queue.is_empty())
queue.clear()
print(queue.is_empty())
