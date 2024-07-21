import sys
input = sys.stdin.readline

from collections import deque



n, k, m = map(int, input().split(' '))
graph = [[] for _ in range(n + m + 1)]

for i in range(1, m + 1) :
    arr = list(map(int, input().split(' ')))
    
    for x in arr :
        graph[x].append(n + i)
        graph[n + i].append(x)

visited = [False] * (n + m + 1)
q = deque([(0, 1)])
found = False

while q :
    cost, now = q.popleft()
    if now == n :
        print(cost // 2 + 1)
        found = True
        break

    for y in graph[now] :
        if not visited[y] :
            visited[y] = True
            q.append((cost + 1, y))

if not found :
    print(-1)
