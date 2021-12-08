class Queue:
    queue = []

    def clear(self):
        self.queue = []

    def is_empty(self) -> bool:
        return True if self.queue == [] else False

    def top(self):
        return self.queue[0] if not self.is_empty() else False

    # Add to end
    def enqueue(self, value):
        self.queue.insert(self.get_length(), value)

    # Grab first item
    def dequeue(self):
        return self.queue.pop(0) if not self.is_empty() else False

    def get_length(self) -> int:
        return len(self.queue)

    def values(self) -> list:
        return self.queue
