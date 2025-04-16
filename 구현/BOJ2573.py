from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j, visited) :
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    dir = {(-1, 0), (1, 0), (0, -1), (0 ,1)}
    while q:
        x, y = q.popleft()
        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0 and not visited[nx][ny] :
                q.append((nx, ny))
                visited[nx][ny] = True

    return visited

def ice_count() :
    visited = [[False] * m for _ in range(n)]

    count = 0
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] != 0 and not visited[i][j] :
                visited = bfs(i, j, visited)
                count += 1

    return count

def melt() :
    q = deque()
    new_arr = [[0] * m for _ in range(n)]

    for i in range(n) :
        for j in range(m) :
            if arr[i][j] != 0 :
                q.append((i, j))

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    while q:
        x, y = q.popleft()
        zero_count = 0
        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0 :
                zero_count += 1

        if arr[x][y] - zero_count > 0 :
            new_arr[x][y] = arr[x][y] - zero_count
        else :
            new_arr[x][y] = 0

    return new_arr


n, m = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

year = 0
while True :
    
    ice = ice_count()
    if 1 < ice :
        print(year)
        break
    elif 0 == ice :
        print(0)
        break

    arr = melt()
    year += 1
    