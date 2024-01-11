

class FIFO:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0


class LIFO:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
      
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None


    def is_empty(self):
        return len(self.stack) == 0
        

