import sys
input = sys.stdin.readline
import heapq

for _ in range(int(input())) :
    n = int(input())
    arr = list(map(int, input().split(' ')))

    heap = []
    for x in arr :
        heapq.heappush(heap, x)

    ans = 0
    while 1 < len(heap) :
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        ans += first + second
        heapq.heappush(heap, first + second)

    print(ans)