import sys
input = sys.stdin.readline

import heapq

k, n = map(int, input().split())
data = list(map(int, input().split()))

heap = []
visited = set()
max_value = max(data)

for x in data :
    heapq.heappush(heap, x)

for i in range(n - 1) :
    min_value = heapq.heappop(heap)

    for x in data :
        now = min_value * x
        
        if len(heap) > n and max_value < now :
            continue
        if now not in visited :
            heapq.heappush(heap, now) 
            max_value = max(max_value, now) 
            visited.add(now)

print(heapq.heappop(heap))