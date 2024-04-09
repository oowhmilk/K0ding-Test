import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

def normal_dfs(x, y, color) :
    normal_visited[x][y] = True
    
    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    for dx, dy in directions :
        nx = x + dx
        ny = y + dy

        if nx < 0 or n <= nx or ny < 0 or n <= ny :
            continue

        if normal_arr[nx][ny] == color and normal_visited[nx][ny] == False :
            normal_dfs(nx, ny, color)


def disable_dfs(x, y, color) :
    disable_visited[x][y] = True
    
    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    for dx, dy in directions :
        nx = x + dx
        ny = y + dy

        if nx < 0 or n <= nx or ny < 0 or n <= ny :
            continue

        if disable_arr[nx][ny] == color and disable_visited[nx][ny] == False :
            disable_dfs(nx, ny, color)


n = int(input())
normal_arr = [[0] * n for _ in range(n)]
normal_visited = [[False] * n for _ in range(n)]
disable_arr = [[0] * n for _ in range(n)]
disable_visited = [[False] * n for _ in range(n)]

for i in range(n) :
    str = input().strip()
    arr = list(str)
    
    for j in range(len(arr)) :
        if arr[j] == 'R' : # 빨강 : 정상 = 0, 비정상 = 0
            normal_arr[i][j] = 0
            disable_arr[i][j] = 0
        elif arr[j] == 'G' : # 초록 : 정상 = 1, 비정상 = 0
            normal_arr[i][j] = 1
            disable_arr[i][j] = 0
        elif arr[j] == 'B' : # 파랑 : 정상 = 2, 비정상 = 2
            normal_arr[i][j] = 2
            disable_arr[i][j] = 2

normal_count = 0
for i in range(n) :
    for j in range(n) :
        if normal_visited[i][j] == False :
            normal_count += 1
            normal_dfs(i, j, normal_arr[i][j])

disable_count = 0
for i in range(n) :
    for j in range(n) :
        if disable_visited[i][j] == False :
            disable_count += 1
            disable_dfs(i, j, disable_arr[i][j])

print(normal_count, disable_count)


import sys
input = sys.stdin.readline

from collections import deque

def normal_bfs(x, y, color) :
    normal_visited[x][y] = True
    deq = deque()
    deq.append((x, y, color))

    while deq :
        x, y, color = deq.popleft()
        
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        for dx, dy in directions :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue

            if normal_arr[nx][ny] == color and normal_visited[nx][ny] == False :
                normal_visited[nx][ny] = True
                deq.append((nx, ny, normal_arr[nx][ny]))


def disable_bfs(x, y, color) :
    disable_visited[x][y] = True
    deq = deque()
    deq.append((x, y, color))

    while deq :
        x, y, color = deq.popleft()
        
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        for dx, dy in directions :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue

            if disable_arr[nx][ny] == color and disable_visited[nx][ny] == False :
                disable_visited[nx][ny] = True
                deq.append((nx, ny, disable_arr[nx][ny]))


n = int(input())
normal_arr = [[0] * n for _ in range(n)]
normal_visited = [[False] * n for _ in range(n)]
disable_arr = [[0] * n for _ in range(n)]
disable_visited = [[False] * n for _ in range(n)]

for i in range(n) :
    str = input().strip()
    arr = list(str)
    
    for j in range(len(arr)) :
        if arr[j] == 'R' : # 빨강 : 정상 = 0, 비정상 = 0
            normal_arr[i][j] = 0
            disable_arr[i][j] = 0
        elif arr[j] == 'G' : # 초록 : 정상 = 1, 비정상 = 0
            normal_arr[i][j] = 1
            disable_arr[i][j] = 0
        elif arr[j] == 'B' : # 파랑 : 정상 = 2, 비정상 = 2
            normal_arr[i][j] = 2
            disable_arr[i][j] = 2

normal_count = 0
for i in range(n) :
    for j in range(n) :
        if normal_visited[i][j] == False :
            normal_count += 1
            normal_bfs(i, j, normal_arr[i][j])

disable_count = 0
for i in range(n) :
    for j in range(n) :
        if disable_visited[i][j] == False :
            disable_count += 1
            disable_bfs(i, j, disable_arr[i][j])

print(normal_count, disable_count)