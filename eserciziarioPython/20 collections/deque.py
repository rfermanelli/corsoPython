import collections
from collections import deque

s = collections.deque([0, 1, 2, 3, 4, 5, 6, 7])

# Queue, FIFO
s.appendleft(10)
print(list(s))
s.pop()
print(list(s))

# Stack, LIFO
s.appendleft(1000)
print(list(s))
s.popleft()
print(list(s))


