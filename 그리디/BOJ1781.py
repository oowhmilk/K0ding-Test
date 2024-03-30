import sys
input = sys.stdin.readline
import heapq

n = int(input())

arr = []
for i in range(n) :
    deadline, cup = map(int, input().split(' '))
    arr.append((deadline, cup))

arr.sort()

heap = []
for i in range(n) :
    deadline, cup = arr[i]
    heapq.heappush(heap, cup)
    
    if len(heap) > deadline :
        heapq.heappop(heap)

print(sum(heap))