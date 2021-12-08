class Stack:
    stack = []

    def clear_stack(self):
        self.stack = []

    def is_empty(self):
        return True if self.stack == [] else False

    def top(self):
        return self.stack[0] if not self.is_empty() else False

    # Add an item to top
    def push(self, value):
        self.stack.insert(0, value)

    # Pop the first item and return
    def pop(self):
        return self.stack.pop(0)

    def get_length(self):
        return len(self.stack)

    def values(self):
        return self.stack
