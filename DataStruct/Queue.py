class Queue:
    queue = []

    def clear(self):
        self.queue = []

    def is_empty(self) -> bool:
        return True if self.queue == [] else False

    def get_top(self):
        return self.queue[0] if not self.is_empty() else False

    # Put value to end
    def put(self, value):
        self.queue.insert(self.get_length(), value)

    # Get value in head
    def get(self):
        return self.queue.pop(0) if not self.is_empty() else False

    def get_length(self) -> int:
        return len(self.queue)

    def values(self) -> list:
        return self.queue
