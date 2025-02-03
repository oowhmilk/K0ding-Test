import heapq
import sys
input = sys.stdin.readline

heap = []

for _ in range(int(input())) :
    x = int(input())
    
    if x == 0 :
        
        if len(heap) == 0 :
            print(0)
        else :
            abs_x, real_x = heapq.heappop(heap)
            print(real_x)

    else :
        heapq.heappush(heap, (abs(x), x))