class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0: # check if array is empty
            return self.items.pop()
        return None

    def peek(self):
        if len(self.items > 0): # check if array is empty
            return self.items[len(self.items) - 1]
        return None

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items)