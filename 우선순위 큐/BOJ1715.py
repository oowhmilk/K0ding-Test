import sys
input = sys.stdin.readline

import heapq

heap = []
for _ in range(int(input())) :
    heapq.heappush(heap, int(input()))

count = 0
while len(heap) != 1 :
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    heapq.heappush(heap, a + b)
    count += a + b

print(count)