from collections import deque
import sys
input = sys.stdin.readline

def bfs() :

    global q
    z, x, y, count = 0, 0, 0, 0

    while q :
        z, x, y, count = q.popleft()

        for dx, dy, dz in dir :
            nx = x + dx
            ny = y + dy
            nz = z + dz

            if nx < 0 or n <= nx or ny < 0 or m <= ny or nz < 0 or h <= nz :
                continue

            if not visited[nz][nx][ny] and arr[nz][nx][ny] == 0 :
                visited[nz][nx][ny] = True
                arr[nz][nx][ny] = 1
                q.append((nz, nx, ny, count + 1))

    return count

m, n, h = map(int, input().split(' '))
arr = [[list(map(int, input().split(' '))) for _ in range(n)] for _ in range(h)]

dir = {(-1, 0, 0), (0, 1, 0), (0, -1, 0), (1, 0, 0), (0, 0, -1), (0, 0, 1)}

visited = [[[False] * m for _ in range(n)] for _ in range(h)]

count = 0
q = deque()
for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if arr[i][j][k] == 1 :
                q.append((i, j, k, 0))
                visited[i][j][k] = True
                
count = bfs()

for i in range(h) :
    for j in range(n) :
        for k in range(m) :
            if arr[i][j][k] == 0 :
                print(-1)
                sys.exit()

print(count)