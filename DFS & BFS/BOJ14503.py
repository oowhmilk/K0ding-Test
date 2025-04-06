from collections import deque 
import sys
input = sys.stdin.readline

def bfs(x, y, now) :
    global result

    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q :
        x, y = q.popleft()

        clean = False
        change = now
        for i in range(4) :
            change = (change + 3) % 4
            dx, dy = dir[change]

            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny] and arr[nx][ny] == 0 :
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    clean = True
                    now = change
                    result += 1
                    break

        if not clean :
            dx, dy = dir[(now + 2) % 4]

            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m :
                if arr[nx][ny] == 1 :
                    print(result)
                    return
                else :
                    visited[nx][ny] = True
                    q.append((nx, ny))



n, m = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

visited = [[False] * m for _ in range(n)]

result = 1
bfs(r, c, d)