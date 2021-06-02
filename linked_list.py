from .node import Node

class LinkedList:

    def __init__(self, root=None):
        self.root = root
        self.size = 0


    # add data
    def add(self, data):
        new_node = Node(data, next_node=self.root)
        self.root = new_node
        self.size +=1


    # find data
    def find(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.data == data:
                return data
            else:
                this_node = this_node.next_node
        return None


    # remove data
    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.data == data:
                if prev_node is not None: # data is in non-root node
                    prev_node.next_node = this_node.next_node
                else: # data is in root node
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node

                







