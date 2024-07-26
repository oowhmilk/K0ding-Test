import sys
input = sys.stdin.readline

import heapq

INF = int(1e9)

def dijkstra(start) :
    heap = []
    distance[start] = 0
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

n, e = map(int, input().split(' '))
arr = [[] for _ in range(n + 1)]

for _ in range(e) :
    a, b, c = map(int, input().split(' '))
    arr[a].append((b, c))
    arr[b].append((a, c))

a, b = map(int, input().split(' '))

distance = [INF] * (n + 1)
dijkstra(1)
d_1_to_a = distance[a]
d_1_to_b = distance[b]

distance = [INF] * (n + 1)
dijkstra(a)
d_a_to_b = distance[b]
d_a_to_n = distance[n]

distance = [INF] * (n + 1)
dijkstra(b)
d_b_to_a = distance[a]
d_b_to_n = distance[n]

route1 = d_1_to_a + d_a_to_b + d_b_to_n
route2 = d_1_to_b + d_b_to_a + d_a_to_n
result = min(route1, route2)

if result >= INF :
    print(-1)
else :
    print(result)