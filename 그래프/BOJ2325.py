# 모든 최단 경로를 구한 뒤
# 최단 경로들에 포함된 간선들을 하나씩 제거
# 제거하면서 매번 다익스트라를 호출하여 문제를 해결

# "다익스트라" 로 최단 경로 구하기
# "BFS" 로 최단 경로에 포함된 모든 간선을 구하기
# 최단 경로에 포함된 모든 간선을 하나씩 지워가면서 매번 "다익스트라" 호출

import sys
input = sys.stdin.readline
import heapq 
from collections import deque

INF = int(1e9)

def dijkstra(a, b) : # 현재 노드와 인접한 다른 
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap :
        dist, now = heapq.heappop(heap)
        if distance[now] < dist :
            continue

        for i in arr[now] :
            if i[0] == a and now == b :
                continue
            elif i[0] == b and now == a :
                continue
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

def bfs() :
    q = deque()
    q.append(end)
    removes = set()
    visited = set()

    while q :
        now = q.popleft()
        if now == end :
            continue

        for i in arr[now] :
            cost = distance[i[0]] + i[1]
            if cost == distance[now] :
                removes.add((i[0], now))

                if i[0] not in visited :
                    visited.add(i[0])
                    q.append(i[0])

    return removes

n, m = map(int, input().split(' '))
start, end = 1, n

arr = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b, c = map(int, input().split(' '))
    arr[a].append((b, c))
    arr[b].append((a, c))

distance = [INF] * (n + 1)
dijkstra(-1, -1)

removes = bfs()

result = 0
for a, b in removes :
    distance = [INF] * (n + 1)
    dijkstra(a, b)
    result = max(result, distance[end])

print(result)





import sys
# 빠른 입력 함수 사용
input = sys.stdin.readline
from collections import deque # 큐 라이브러리 
import heapq # 우선순위 큐 라이브러리
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
# 일반적인 다익스트라와 동일하지만, a ↔ b 간선은 무시하는 함수
def dijkstra(a, b): 
    q = []
# 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start)) 
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist: continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인 
    for i in graph[now]:
    # a ↔ b 간선은 무시
        if i[0] == a and now == b: continue
        elif i[0] == b and now == a: continue
        cost = dist + i[1]
# 현재 노드를 거쳐, 다른 노드로 가는 거리가 더 짧으면 
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

def bfs():
    q = deque()
    visited = set() # 특정한 노드 방문 여부 
    q.append(end) # 도착 지점(end)을 큐에 삽입 
    removes = set() # 삭제할 간선들(결과) 
    while q:
        now = q.popleft()
        if now == start:
            continue
        for i in graph[now]: # 현재 노드와 연결된 간선들 확인 
            cost = distance[i[0]] + i[1]
        # 최단 경로에 포함된 간선인 경우 삭제 목록에 추가 
            if cost == distance[now]:
                removes.add((i[0], now))
        # 각 "직전 노드"는 한 번씩만 방문 
                if i[0] not in visited:
                    q.append(i[0])
                    visited.add(i[0])
    return removes

n, m = map(int, input().split())
# 시작 노드와 도착 노드
start, end = 1, n
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 
graph = [[] for i in range(n + 1)]
# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
# a번 노드에서 b번 노드로 가는 비용이 c라는 의미 
    graph[a].append((b, c))
    graph[b].append((a, c))


distance = [INF] * (n + 1)
# 다익스트라 알고리즘을 수행 
dijkstra(-1, -1)
# 최단 경로 역추적 수행
# 모든 최단 경로에 포함된 간선 쌍 (a, b)들을 계산 
removes = bfs()
result = 0
# 모든 최단 경로에 포함된 간선 쌍 (a, b)들을 확인 
for a, b in removes:
# 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n + 1)
    # a ↔ b 간선은 무시하는 다익스트라 알고리즘을 수행 
    dijkstra(a, b)
    result = max(result, distance[end])
print(result)