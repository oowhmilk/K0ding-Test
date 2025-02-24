from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

arr = []
for _ in range(m) :
    arr.append(list(map(int, input().split(' '))))

visited = [[-1] * n for _ in range(m)]
q = deque()
for i in range(m) :
    for j in range(n) :
        if arr[i][j] == 1 :
            q.append((i, j))
            visited[i][j] = 0

dir = {(-1, 0), (0, -1), (0, 1), (1, 0)}
while q :
    x, y = q.popleft()
    
    for dx, dy in dir :
        nx = x + dx
        ny = y + dy

        if nx < 0 or m <= nx or ny < 0 or n <= ny :
            continue

        if arr[nx][ny] == 0 and visited[nx][ny] == -1 :
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

max_value = -1
for i in range(m) :
    for j in range(n) :
        if visited[i][j] == -1 and arr[i][j] != -1:
            print(-1)
            sys.exit()
        max_value = max(max_value, visited[i][j])

print(max_value)