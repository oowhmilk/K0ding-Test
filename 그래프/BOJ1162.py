# "다익스트라" 를 사용하며, 방문한는 각 노드까지의 최단 거리를 DP xpdlqmfdp rlfhr
# 각 노드에 대해 distance[노드번호][현재까지 포장 횟수] 를 갱신
# 해당 노드를 포장할지 안 할지 결정하는 방식

import sys
input = sys.stdin.readline

import heapq

INF = int(1e17)

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 1, 0))
    distance[1][0] = 0

    while heap :
        dist, now, paved = heapq.heappop(heap)
        if distance[now][paved] < dist : # 현재 노드가 처리된적 있는 노드라면 무시
            continue
        for i in arr[now] : # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]
            if cost < distance[i[0]][paved] : # 포장하지 않는 경우
                distance[i[0]][paved] = cost
                heapq.heappush(heap, (cost, i[0], paved))
            if paved < k and dist < distance[i[0]][paved + 1] : # 포장하는 경우 (cost 대신 dist 사용) => 해당 간선이 포장되어있어서 cost 값이 아닌 dist + 0 을 더한 값이 들어간다고 생각
                distance[i[0]][paved + 1] = dist
                heapq.heappush(heap, (dist, i[0], paved + 1))


n, m, k = map(int, input().split(' '))
arr = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b, cost = map(int, input().split(' '))
    arr[a].append((b, cost))
    arr[b].append((a, cost))

distance = [[INF] * (k + 1) for _ in range(n + 1)]
dijkstra()

result = INF
for i in range(k + 1) :
    result = min(result, distance[n][i])

print(result)