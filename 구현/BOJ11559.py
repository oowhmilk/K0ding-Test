from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, value) :
    global flag
    boom = []

    q = deque()
    q.append((x, y))
    boom.append((x, y))
    visited[x][y] = True

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    count = 1
    while q :
        x, y = q.popleft()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or 12 <= nx or ny < 0 or 6<= ny :
                continue

            if not visited[nx][ny] and arr[nx][ny] == value :
                q.append((nx, ny))
                visited[nx][ny] = True
                boom.append((nx, ny))
                count += 1

    if 4 <= count :
        flag = True
        for b in boom :
            arr[b[0]][b[1]] = '.'

def down() :
    for i in range(6) :
        rotate = deque()

        for j in range(11, -1, -1) :
            if arr[j][i] != '.' :
                rotate.append(arr[j][i])
        
        for j in range(11, -1, -1) :
            if rotate :
                arr[j][i] = rotate.popleft()
            else :
                arr[j][i] = '.'

arr = []
for _ in range(12) :
    arr.append(list(input().strip()))

time = 0
while True :

    flag = False
    visited = [[False] * 6 for _ in range(12)]

    for i in range(12) :
        for j in range(6) :
            if arr[i][j] != '.' :
                bfs(i, j, arr[i][j])

    down()

    if not flag :
        break
    else :
        time += 1

print(time)