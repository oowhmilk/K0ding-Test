import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y, cnt) :
    q = deque()
    q.append((x, y, cnt))
    visited[x][y] = True

    dir = {(0, 1), (1, 0), (0, -1), (-1, 0)}
    while q :
        x, y, cnt = q.popleft()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or m <= ny :
                continue

            if x == n - 1 and y == m - 1 :
                return cnt
        
            if arr[nx][ny] == 1 and not visited[nx][ny] :
                q.append((nx, ny, cnt + 1))
                visited[nx][ny] = True

n, m = map(int, input().split(' '))
arr = [[] for _ in range(n)]
for i in range(n) :
    str = input().strip()
    
    for j in range(len(str)) :
        arr[i].append(int(str[j]))

visited = [[False] * m for _ in range(n)]
print(bfs(0, 0, 1))
