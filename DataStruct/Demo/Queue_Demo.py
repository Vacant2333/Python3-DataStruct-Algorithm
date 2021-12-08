from DataStruct.Queue import Queue

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Values: {}".format(queue.values()))
print("Pop: {}".format(queue.dequeue()))
queue.enqueue(4)
print("Get top:{}".format(queue.top()))

print(queue.get_length())
print(queue.values())
print(queue.is_empty())
queue.clear()
print(queue.is_empty())
