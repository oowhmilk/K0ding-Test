import sys
input = sys.stdin.readline

import heapq

n, k = map(int, input().split(' '))
jew = []
bag = []

for _ in range(n) :
    m, v = map(int, input().split(' '))
    jew.append((m, v))

for _ in range(k) :
    bag.append(int(input()))

jew.sort()
bag.sort()

heap = []
cur = 0
result = 0

for x in bag :
    while cur < n :
        m, v = jew[cur]
        if x >= m :
            heapq.heappush(heap, -v)
            cur += 1
        else : 
            break
        
    if len(heap) > 0 :
        result += heapq.heappop(heap) * (-1)

print(result)