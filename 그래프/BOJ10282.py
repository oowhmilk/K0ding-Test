## 다익스트라 알고리즘
## 그래프 간 최단거리 문제 풀때 사용
## 시작점 부터 각 점들까지 최단거리 == 최소 비용
## 모든 점들 사이 거리 값을 1e9 로 초기화 후
## 이동할 점과 현재 점에서 이동 비용을 합한 값 vs 이동할 점 비용 값 비교해서 작은 값을 채택
## heapq 우선순위 큐 이용해서 최단거리라고 판단하면 heapq 에 삽입

import sys
input = sys.stdin.readline
import heapq

def dijkstra(start) :
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0

    while heap_data :
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist :
            continue
        for i in arr[now] :
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))
    

for _ in range(int(input())) :
    n, d, c = map(int, input().split(' ')) # n : 컴퓨터 개수, d : 의존성 개수, c : 해킹당한 컴퓨터의 번호
    arr = [[] for i in range(n + 1)]  # 컴퓨터 번호를 1부터 시작하므로 크기를 n + 1로 설정
    distance = [1e9] * (n + 1)

    for _ in range(d) :
        a, b, s = map(int, input().split(' ')) # a : 도착 노드, b : 시작 노드, s : 거리
        arr[b].append((a, s))

    dijkstra(c)
    count = 0
    max_distance = 0
    for i in distance :
        if i != 1e9 :
            count += 1
            if i > max_distance :
                max_distance = i

    print(count, max_distance)
