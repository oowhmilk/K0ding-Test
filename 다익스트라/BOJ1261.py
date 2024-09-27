import sys
input = sys.stdin.readline

import heapq

def bfs(x, y) :

    q = []
    heapq.heappush(q, (0, x, y))
    visited[x][y] = True

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    while q :
        count, x, y = heapq.heappop(q)

        if x == n - 1 and y == m - 1 :
            return count

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy 

            if nx < 0 or n <= nx or ny < 0 or m <= ny :
                continue

            if not visited[nx][ny] :
                if arr[nx][ny] == '1' :
                    visited[nx][ny] = True
                    heapq.heappush(q, (count + 1, nx, ny))
                else :
                    visited[nx][ny] = True
                    heapq.heappush(q, (count, nx, ny))


m, n = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(input().strip()))

visited = [[False] * m for _ in range(n)]
print(bfs(0, 0))