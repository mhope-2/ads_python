from stack import Stack

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
