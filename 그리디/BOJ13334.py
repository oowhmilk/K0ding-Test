import sys
input = sys.stdin.readline

import heapq

n = int(input()) 
heap = []

for _ in range(n) :
    h, o = map(int, input().split(' '))
    start = 0
    finsih = 0
    if h > o :
        start = o
        finish = h
    else :
        start = h
        finish = o
    heapq.heappush(heap, (finish - start, start, finish))

d = int(input())

print(heap)