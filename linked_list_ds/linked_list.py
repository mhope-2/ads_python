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

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next() 
        
    def search(self, item):
        current = self.head
        found = False

        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    
    def remove():
        pass