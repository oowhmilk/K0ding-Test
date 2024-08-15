# import sys
# input = sys.stdin.readline

# import heapq
# heap = []
# n = int(input())

# for _ in range(n) :
#     num = int(input())

#     if num == 0:
#         if len(heap) == 0 :
#             print(0)
#         else :
#             absolute, original = heapq.heappop(heap)
#             print(original) 
#     else :
#         heapq.heappush(heap, (abs(num), num))

import sys
input = sys.stdin.readline

import heapq

n = int(input())
heap = []

for _ in range(n) :
    x = int(input())

    if x == 0 :
        if len(heap) == 0 :
            print(0)
        else : 
            absolute, real = heapq.heappop(heap)
            print(real)

    else :
        heapq.heappush(heap, (abs(x), x))