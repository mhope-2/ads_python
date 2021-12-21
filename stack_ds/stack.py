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
        if len(self.items) > 0: # check if array is empty
            return self.items[len(self.items) - 1]
        return None

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def __str__(self) -> str:
        return str(self.items)

if __name__ == '__main__':
    my_stack = Stack()

    print("created my_stack")
    print(my_stack)

    print(my_stack.is_empty())

    my_stack.push(1)
    print(my_stack)

    my_stack.push(5)
    print(my_stack)

    my_stack.push(8)
    print(my_stack)

    my_stack.push(9)
    print(my_stack)


    my_stack.pop()
    print(my_stack)

    print(my_stack.peek())

    print(my_stack.is_empty())

    print(my_stack.size())

    ##############################

    my_stack.pop()
    print(my_stack)

    my_stack.pop()
    print(my_stack)

    my_stack.pop()
    print(my_stack)

    my_stack.pop()
    print(my_stack)


    my_stack.pop()
    print(my_stack)

    my_stack.pop()
    print(my_stack)

    my_stack.pop()
    print(my_stack)

    my_stack.pop()
    print(my_stack)