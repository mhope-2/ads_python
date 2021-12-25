class Queue:
    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop()
        return None
    
    def is_empty(self):
        return self.items == []

    
    def size(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items)

if __name__ == '__main__':
    queue = Queue()

    print(queue.is_empty())
    queue.enqueue(4)
    queue.enqueue('dog')
    queue.enqueue(True)
    print(queue.size())
    print(queue.is_empty())
    queue.enqueue(8.4)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.size())

