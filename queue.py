from collections import deque

my_queue = deque()
my_queue.append(3) # add item to the end
my_queue.append(10) 
print(my_queue)
print(my_queue.popleft()) # pop item from the front