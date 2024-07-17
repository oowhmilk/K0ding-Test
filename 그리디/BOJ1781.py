# 데드라인을 초과하는 문제를 풀 수 없다. 
# 정렬과 우선 순위 큐 => O(NlogN)

# import sys
# input = sys.stdin.readline
# import heapq

# n = int(input())

# arr = []
# for i in range(n) :
#     deadline, cup = map(int, input().split(' '))
#     arr.append((deadline, cup))

# arr.sort()

# heap = []
# for i in range(n) :
#     deadline, cup = arr[i]
#     heapq.heappush(heap, cup)
    
#     if len(heap) > deadline :
#         heapq.heappop(heap)

# print(sum(heap))



import sys
input = sys.stdin.readline
import heapq

n = int(input())

arr = []
for _ in range(n) :
    deadline, noodle = map(int, input().split(' '))
    arr.append((deadline, noodle))

arr.sort()

heap = []
time = 0
for i in range(n) :
    # deadline, noodle = arr[i]
    # print(arr[i][1])
    heapq.heappush(heap, arr[i][1])

    if len(heap) > arr[i][0] :
        heapq.heappop(heap)

print(heap)
result = 0
for i in range(len(heap)) :
    result += heapq.heappop(heap)

print(result)