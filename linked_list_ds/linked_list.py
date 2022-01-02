from .node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
      temp = Node(item)
      temp.set_next(self.head)
      self.head = temp