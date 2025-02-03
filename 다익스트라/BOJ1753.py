import heapq
import sys
input = sys.stdin.readline

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

v, e = map(int, input().split(' '))
k = int(input())

arr = [[] for _ in range(v + 1)]
for _ in range(e) :
    a, b, c = map(int, input().split(' '))
    arr[a].append((b, c))

distance = [int(1e9)] * (v + 1)

dijkstra(k)

for i in range(1, v + 1) :
    if distance[i] != int(1e9) :
        print(distance[i])
    else :
        print("INF")