import heapq
import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n) :
    start, end = map(int, input().split(' '))
    arr.append((start, end))
arr.sort(key = lambda x : (x[0], x[1]))

heap = [arr[0][1]]

for i in range(1, n) :

    if arr[i][0] < heap[0] :
        heapq.heappush(heap, arr[i][1])
    else :
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])

print(len(heap))