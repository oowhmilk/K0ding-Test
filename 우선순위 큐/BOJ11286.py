import sys
input = sys.stdin.readline

import heapq
heap = []
n = int(input())

for _ in range(n) :
    num = int(input())

    if num == 0:
        if len(heap) == 0 :
            print(0)
        else :
            absolute, original = heapq.heappop(heap)
            print(original) 
    else :
        heapq.heappush(heap, (abs(num), num))