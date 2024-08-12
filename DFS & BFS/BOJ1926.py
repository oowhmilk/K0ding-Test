import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y) :
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    size = 1

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    while q :
        x, y = q.popleft()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or m <= ny :
                continue

            if arr[nx][ny] == 1 and not visited[nx][ny] :
                visited[nx][ny] = True
                q.append((nx, ny))
                size += 1

    return size


n, m = map(int, input().split(' '))
arr = []

for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

max_size = 0
count = 0
visited = [[False] * m for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 1 and not visited[i][j] :
            size = bfs(i, j)
            count += 1
            max_size = max(max_size, size)

print(count)
print(max_size)