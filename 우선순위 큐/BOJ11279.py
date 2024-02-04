import sys
input = sys.stdin.readline

import heapq

n = int(input())

abs_heap = []

for _ in range(n) :
    x = int(input())

    if x == 0 :
        if len(abs_heap) == 0 :
            print(0)
        else :
            count = heapq.heappop(abs_heap)
            print(-1 * count)
    else :
        heapq.heappush(abs_heap, -1 * x)

