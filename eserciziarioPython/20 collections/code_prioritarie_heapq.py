import heapq

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

heapq.heappush(l, 100)
print(list(l))

x = heapq.heappop(l)
print(x)
