from Sorting.DataStruct.Stack import Stack
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print("Values: {}".format(stack.values()))
print("Pop: {}".format(stack.pop()))
stack.push(4)
print("Get top:{}".format(stack.get_top()))

print(stack.get_length())
print(stack.values())
print(stack.is_empty())
stack.clear_stack()
print(stack.is_empty())
