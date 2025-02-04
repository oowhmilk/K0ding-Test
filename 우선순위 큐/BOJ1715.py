import heapq
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())) :
    x = int(input())
    heapq.heappush(heap, x)

count = 0
while 2 <= len(heap) :
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    count += a + b
    heapq.heappush(heap, a + b)

print(count)