import sys
input = sys.stdin.readline
import heapq

n = int(input())

arr = []

for i in range(n) :
    num, start, end = map(int, input().split())
    heapq.heappush(arr, (start, end))

heap = []
end = heapq.heappop(arr)[1]
heapq.heappush(heap, end)
ans = 1

for i in range(n - 1) :
    new_start, new_end = heapq.heappop(arr)

    end = heapq.heappop(heap)

    if new_start < end :
        heapq.heappush(heap, end)
        heapq.heappush(heap, new_end)
        ans += 1
    else : 
        heapq.heappush(heap, new_end)

print(ans)