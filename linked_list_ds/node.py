class Node:
    def __init__(self, init_data) -> None:
        self.data = init_data
        self.next = None
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next
    
    def __str__(self):
        return ( '( {} )'.format(self.data))

if __name__ == '__main__':
    node = Node(89)
    print(node.get_data())
    print(node)