import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split(' '))
arr = []

for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

q = deque()
visited = [[0] * m for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 1 :
            q.append((i, j))
            visited[i][j] = 1
        elif arr[i][j] == -1 :
            visited[i][j] = -1

while q :
    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    x, y = q.popleft()

    for dx, dy in dir :
        nx = x + dx
        ny = y + dy 

        if nx < 0 or n <= nx or ny < 0 or m <= ny :
            continue

        if arr[nx][ny] == 0 and visited[nx][ny] == 0 :
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

for i in range(n) :
    for j in range(m) :
        if visited[i][j] == 0 :
            print(-1)
            sys.exit()

max_value = -1
for i in range(n) :
    for j in range(m) :
        max_value = max(max_value, visited[i][j])

print(max_value - 1)