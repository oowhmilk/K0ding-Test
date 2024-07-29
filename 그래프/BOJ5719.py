import sys
input = sys.stdin.readline

import heapq

from collections import deque

INF = int(1e9)

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

def bfs(v) :
    q = deque()
    q.append(v)
    visited = [False] * (n)
    visited[v] = True
    removes = set()

    while q :
        v = q.popleft()
        if v == start :
            break

        for i in reversed_arr[v] :
            cost = distance[i[0]] + i[1]
            if cost == distance[v] :
                removes.add((i[0], v))

                if not visited[i[0]] :
                    visited[i[0]] = True
                    q.append(i[0])

    return removes


while 1 :
    n, m = map(int, input().split(' '))
    if n == 0 and m == 0 :
        break

    start, end = map(int, input().split(' '))

    arr = [[] for _ in range(n)]
    reversed_arr = [[] for _ in range(n)]

    for _ in range(m) :
        u, v, p = map(int, input().split(' '))
        arr[u].append((v, p))
        reversed_arr[v].append((u, p))

    distance = [INF] * (n)
    dijkstra(start)

    removes = bfs(end)

    new_arr = [[] for _ in range(n)]
    for a in range(n) :
        for b, c in arr[a] :
            if (a, b) not in removes :
                new_arr[a].append((b, c))
    arr = new_arr

    distance = [INF] * (n)
    dijkstra(start)

    if distance[end] == INF :
        print(-1)
    else : 
        print(distance[end])
    

    