import sys
input = sys.stdin.readline

from itertools import combinations

from collections import deque

def bfs(selected) :
    global answer
    visited = [[-1] * n for _ in range(n)]
    q = deque()

    for x, y in selected :
        q.append((x, y))
        visited[x][y] = 0

    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    cnt = 0
    while q :
        x, y = q.popleft()
        for dx, dy in directions :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue
            if visited[nx][ny] == -1 and arr[nx][ny] != 1 :
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                if arr[nx][ny] == 0 :
                    cnt += 1
                    
    taken = 0
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 0 :
                taken = max(taken, visited[i][j])
    if cnt == target :
        answer = min(taken, answer)

n, m = map(int, input().split(' '))
arr = []
virus = []
target = 0
answer = int(1e9)

for i in range(n) :
    arr.append(list(map(int, input().split(' '))))
    for j in range(n) :
        if arr[i][j] == 2 :
            virus.append((i, j))
        if arr[i][j] == 0 :
            target += 1
        
comb = list(combinations(virus, m))

for selected in comb :
    bfs(selected)

if answer == int(1e9) :
    print(-1)
else :
    print(answer)