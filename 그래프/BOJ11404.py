# 모든 도시의 쌍에 대해 도시 A 에서 B 로 가는데 필요한 최소 비용을 모두 구함
# 모든 도시의 쌍이기 때문에 "플로이드 워셜" 알고리즘 사용
# 기존처러 단순 A 에서 B 로 가는 최소 비용을 구할때는 "다익스트라" 알고리즘 사용

import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1) :
    for j in range(n + 1) :
        if i == j :
            graph[i][j] = 0

for _ in range(m) :
    a, b, c = map(int, input().split(' '))
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1) :
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if graph[i][j] == 1e9 :
            print(0, end = " ")
        else :
            print(graph[i][j], end = " ")

    print()