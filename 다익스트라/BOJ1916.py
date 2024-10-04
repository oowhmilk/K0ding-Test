# import sys
# import heapq
# input = sys.stdin.readline

# def dijkstra(start) :
#     heap = []
#     heapq.heappush(heap, (0, start))
#     distance[start] = 0

#     while heap :
#         dist, now = heapq.heappop(heap)

#         if distance[now] < dist :
#             continue

#         for i in arr[now] :
#             cost = dist + i[1]
#             if cost < distance[i[0]] :
#                 distance[i[0]] = cost
#                 heapq.heappush(heap, (cost, i[0]))

# n = int(input())
# m = int(input())

# arr = [[] for _ in range(n + 1)]
# for _ in range(m) :
#     a, b, c = map(int, input().split(' '))
#     arr[a].append((b, c))

# start, end = map(int, input().split(' '))

# distance = [int(1e9)] * (n + 1)
# dijkstra(start)

# print(distance[end])



# import sys
# import heapq
# input = sys.stdin.readline

# def dijkstra(start) :
#     heap = []
#     heapq.heappush(heap, (0, start))
#     distance[start] = 0

#     while heap :
#         dist, x = heapq.heappop(heap)

#         if distance[x] < dist :
#             continue
        
#         for i in arr[x] :
#             cost = dist + i[1]

#             if cost < distance[i[0]] :
#                 distance[i[0]] = cost
#                 heapq.heappush(heap, (cost, i[0]))

# n = int(input())
# m = int(input())

# arr = [[] for _ in range(n + 1)]
# for _ in range(m) :
#     a, b, c = map(int, input().split(' '))
#     arr[a].append((b, c))

# start, end = map(int, input().split(' '))

# distance = [int(1e9)] * (n + 1)
# dijkstra(start)
# print(distance[end])


import sys
input = sys.stdin.readline
import heapq

def dijkstra(start) :
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap :
        dist, now = heapq.heappop(heap)

        if distance[now] < dist :
            continue

        for i in arr[now] :
            cost = dist + i[1]

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]
for _ in range(m) :
    a, b, c = map(int, input().split(' '))
    arr[a].append((b, c))

start, end = map(int, input().split(' '))
distance = [int(1e9)] * (n + 1)
dijkstra(start)
print(distance[end])