import sys
input = sys.stdin.readline

from collections import deque

def bfs() :
    while q :
        x, y = q.popleft()

        dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for (dx, dy) in dir :
            nx = x + dx
            ny = y + dy 

            if nx < 0 or n <= nx or ny < 0 or m <= ny :
                continue
            if graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))



n, m = map(int, input().split(' '))
graph = []
visited = [[False] * m for _ in range(n)]

for _ in range(n) :
    arr = list(map(int, input().split(' ')))
    graph.append(arr)


q = deque()

for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 1 :
            q.append((i, j))

bfs()

result = 0
for i in range(n) :
    for j in range(m) :
        result = max(result, graph[i][j])

print(result - 1)