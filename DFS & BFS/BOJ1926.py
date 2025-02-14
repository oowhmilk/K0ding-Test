from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y) :
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    dir = {(-1, 0), (0, -1), (1, 0), (0, 1)}
    size = 0
    while q :
        x, y = q.popleft()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or n <= nx or ny < 0 or m <= ny :
                continue

            if arr[nx][ny] == 1 and not visited[nx][ny] :
                q.append((nx, ny))
                visited[nx][ny] = True
                size += 1

    return size + 1

n, m = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

visited = [[False] * m for _ in range(n)]

count = 0
max_size = 0
for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 1 and not visited[i][j] :
            size = bfs(i, j)
            count += 1
            max_size = max(max_size, size)

print(count)
print(max_size)