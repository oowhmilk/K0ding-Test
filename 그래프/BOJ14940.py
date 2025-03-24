from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y) :
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    while q :
        x, y = q.popleft()
        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m :
                if visited[nx][ny] == -1 and arr[nx][ny] == 1 :
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

n, m = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))


visited = [[-1] * m for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 2 :
            start_x = i
            start_y = j
        if arr[i][j] == 0 :
            visited[i][j] = 0

bfs(start_x, start_y)

for i in range(n) :
    for j in range(m) :
        print(visited[i][j], end = ' ')
    print()