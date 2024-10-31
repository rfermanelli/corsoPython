from queue import PriorityQueue

q = PriorityQueue()
print(q.qsize())
print(q.empty())
print(q.full())
q.put(100)
q.put(20)
x = q.get_nowait()

print(x)



