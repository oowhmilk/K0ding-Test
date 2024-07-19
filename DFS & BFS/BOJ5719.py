# 최단 경로를 구하는 알고리즘
# 최단 경로를 구하기 위해서는 최단 거리 == 최단 비용이 얼마인지 알아야 한다.
# 다익스트라 알고리즘을 통해 시작점으로 부터 모든 정점들 간의 최단 거리 배열을 만든다.
# 끝점을 기준으로 BFS 를 이용하요 최단경로에 포함되어 있는 모든 간선을 역으로 추적 할 수 있다. 
# 정점으로 간선들을 확인한 다음에 역으로 전 정점들을 확인할 수 있다.
# 확인한 정점들이 맞다면 deque 에서 빼고 전 정점들을 넣어주면 된다. 

import sys
input = sys.stdin.readline
from collections import deque
import heapq

def dijkstra() :
    heap_data = []
    heapq.heappush(heap_data, (0, s))
    distance[s] = 0

    while heap_data :
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist :
            continue
        for i in adj[now] :
            cost = dist + i[1]
            if distance[i[0]] > cost and not dropped[now][i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))


def bfs() :
    q = deque()
    q.append(d)
    while q :
        now = q.popleft()
        if now == s :
            continue
        for prev, cost in reverse_adj[now] :
            if distance[now] == distance[prev] + cost and dropped[prev][now] == False:
                dropped[prev][now] = True
                q.append(prev)


while 1 :
    n, m = map(int, input().split(' '))

    if n == 0 :
        break

    s, d = map(int, input().split(' '))

    adj = [[] for _ in range(n + 1)]
    reverse_adj = [[] for _ in range(n + 1)]

    for _ in range(m) :
        u, v, p = map(int, input().split(' '))
        adj[u].append((v, p))
        reverse_adj[v].append((u, p))

    dropped = [[False] * (n + 1) for _ in range(n + 1)]
    distance = [1e9] * (n + 1)
    dijkstra()
    bfs()
    distance = [1e9] * (n + 1)
    dijkstra()

    if distance[d] != 1e9 :
        print(distance[d])
    else :
        print(-1)