from collections import deque
import sys
input = sys.stdin.readline

def cal(check) :

    global arr

    check = list(check)

    total = 0
    for x, y in check :
        total += arr[x][y]

    for x, y in check :
        arr[x][y] = total // len(check)
    

def bfs(x, y) :

    global change

    q = deque()
    check = set()

    q.append((x, y))
    check.add((x, y))
    visited[x][y] = True

    dir = {(-1, 0), (0, 1), (0, -1), (1, 0)}
    while q : 
        x, y = q.popleft()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy 

            if 0 <= nx < n and 0 <= ny < n :
                if not visited[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r :
                    q.append((nx, ny))
                    check.add((nx, ny))
                    visited[nx][ny] = True

    if 1 < len(check) :
        cal(check)
        change = True
        


n, l, r = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

answer = 0
while True :

    change = False
    visited = [[False] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                bfs(i, j)

    if change :
        answer += 1
    else : 
        break

print(answer)