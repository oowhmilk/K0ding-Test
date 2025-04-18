from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j) :
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    count = 0

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    while q :
        count += 1
        x, y = q.popleft()
        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = True

    return count

m, n, k = map(int, input().split(' '))
square = []
for _ in range(k) :
    a, b, c, d = map(int, input().split(' '))
    x1, y1, x2, y2 = (m - 1) - b, a, (m - 1) - (d - 1), (c - 1)
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    square.append((min_x, min_y, max_x, max_y))

arr = [[0] * n for _ in range(m)]
for sq in square :
    x1, y1, x2, y2 = sq
    for i in range(x1, x2 + 1) :
        for j in range(y1, y2 + 1) :
            arr[i][j] = 1

visited = [[False] * n for _ in range(m)]
total = 0
result = []
for i in range(m) :
    for j in range(n) :
        if arr[i][j] == 0 and not visited[i][j]:
            total += 1
            result.append(bfs(i, j))

print(total)
result.sort()
for x in result :
    print(x, end = ' ')