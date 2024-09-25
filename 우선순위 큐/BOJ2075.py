import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n) : 
    arr = list(map(int, input().split(' ')))

    for i in range(len(arr)) :
        heapq.heappush(heap, arr[i])
        if len(heap) > n :
            heapq.heappop(heap)

print(heapq.heappop(heap))