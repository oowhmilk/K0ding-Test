import sys
input = sys.stdin.readline

import heapq

def dijkstra(start) :
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap :
        dist, now = heapq.heappop(heap)
        if distance[now] < dist :
            continue

        
        for i in arr[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


n, m, x = map(int, input().split(' '))

arr = [[] for _ in range(n + 1)]
for _ in range(m) :
    a, b, c = map(int, input().split(' '))
    arr[a].append((b, c))

go = [0]
back = []

for i in range(n) :
    distance = [int(1e9)] * (n + 1)
    dijkstra(i + 1)

    if i + 1 == x :
        back = distance
        go.append(0)
    else :
        go.append(distance[x])

max_size = -1
for i in range(n + 1) :
    result = go[i] + back[i]
    if result < 1000000000 :
        max_size = max(result, max_size)

print(max_size)