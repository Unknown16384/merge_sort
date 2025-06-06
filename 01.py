class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def peek(self):
        if not self.is_empty(): return self.items[0]
    def dequeue(self):
        if not self.is_empty(): return self.items.pop(0)