class Stack:
    def __init__(self):
        self.stack = list()
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if len(self.stack > 0):
            return self.stack.pop()
        return None
    
    def peek(self):
        if len(self.stack > 0):
            return self.stack[-1]
        return None
    
    def __str__(self):
        return str(self.stack)