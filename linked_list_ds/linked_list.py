from .node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        # self.size = 0

    
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
      temp = Node(item)
      temp.set_next(self.head)
      self.head = temp
    #   self.size += 1

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next() 
        

    
    def remove():
        pass