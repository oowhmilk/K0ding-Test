from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y) :
    global height
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    while q :
        x, y = q.popleft()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy 

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue

            if not visited[nx][ny] and height < arr[nx][ny] :
                visited[nx][ny] = True
                q.append((nx, ny))


n = int(input())
arr = []

max_value = 0

for _ in range(n) :
    check = list(map(int, input().split(' ')))
    max_value = max(max_value, max(check))
    arr.append(check)

result = 0
for height in range(max_value) :
    visited = [[False] * n for _ in range(n)]

    count = 0
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] and height < arr[i][j] :
                count += 1
                bfs(i, j)

    result = max(result, count)

print(result)