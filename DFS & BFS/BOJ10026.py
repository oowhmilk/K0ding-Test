# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(100000)

# def normal_dfs(x, y) :
#     global color

#     dir = {(-1, 0), (1 , 0), (0, -1), (0, 1)}
#     visited[x][y] = True

#     for dx, dy in dir :
#         nx = x + dx
#         ny = y + dy

#         if nx < 0 or n <= nx or ny < 0 or n <= ny :
#             continue

#         if normal[nx][ny] == color and not visited[nx][ny] :
#             normal_dfs(nx, ny)

# def ab_normal_dfs(x, y) :
#     global color

#     dir = {(-1, 0), (1 , 0), (0, -1), (0, 1)}
#     visited[x][y] = True

#     for dx, dy in dir :
#         nx = x + dx
#         ny = y + dy

#         if nx < 0 or n <= nx or ny < 0 or n <= ny :
#             continue

#         if ab_normal[nx][ny] == color and not visited[nx][ny] :
#             ab_normal_dfs(nx, ny)


# n = int(input())
# normal = [[0] * (n) for _ in range(n)]
# ab_normal = [[0] * (n) for _ in range(n)]
# visited = [[False] * (n) for _ in range(n)]

# for i in range(n) :
#     str = input().strip()
#     change = list(str)

#     for j in range(n) :
#         if change[j] == 'R' : #
#             normal[i][j] = 0
#         elif change[j] == 'G' : 
#             normal[i][j] = 1
#         else :
#             normal[i][j] = 2

#     for j in range(n) :
#         if change[j] == 'R' : #
#             ab_normal[i][j] = 0
#         elif change[j] == 'G' : 
#             ab_normal[i][j] = 0
#         else :
#             ab_normal[i][j] = 2


# normal_result = 0
# for i in range(n) :
#     for j in range(n) :
#         if not visited[i][j] :
#             normal_result += 1
#             color = normal[i][j]
#             normal_dfs(i, j)


# visited = [[False] * (n) for _ in range(n)]
# ab_normal_result = 0
# for i in range(n) :
#     for j in range(n) :
#         if not visited[i][j] :
#             ab_normal_result += 1
#             color = ab_normal[i][j]
#             ab_normal_dfs(i, j)

# print(normal_result, end = ' ')
# print(ab_normal_result)

# import sys
# input = sys.stdin.readline

# from collections import deque

# def normal_bfs(x, y, color) :
#     normal_visited[x][y] = True
#     deq = deque()
#     deq.append((x, y, color))

#     while deq :
#         x, y, color = deq.popleft()
        
#         directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
#         for dx, dy in directions :
#             nx = x + dx
#             ny = y + dy

#             if nx < 0 or n <= nx or ny < 0 or n <= ny :
#                 continue

#             if normal_arr[nx][ny] == color and normal_visited[nx][ny] == False :
#                 normal_visited[nx][ny] = True
#                 deq.append((nx, ny, normal_arr[nx][ny]))


# def disable_bfs(x, y, color) :
#     disable_visited[x][y] = True
#     deq = deque()
#     deq.append((x, y, color))

#     while deq :
#         x, y, color = deq.popleft()
        
#         directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
#         for dx, dy in directions :
#             nx = x + dx
#             ny = y + dy

#             if nx < 0 or n <= nx or ny < 0 or n <= ny :
#                 continue

#             if disable_arr[nx][ny] == color and disable_visited[nx][ny] == False :
#                 disable_visited[nx][ny] = True
#                 deq.append((nx, ny, disable_arr[nx][ny]))


# n = int(input())
# normal_arr = [[0] * n for _ in range(n)]
# normal_visited = [[False] * n for _ in range(n)]
# disable_arr = [[0] * n for _ in range(n)]
# disable_visited = [[False] * n for _ in range(n)]

# for i in range(n) :
#     str = input().strip()
#     arr = list(str)
    
#     for j in range(len(arr)) :
#         if arr[j] == 'R' : # 빨강 : 정상 = 0, 비정상 = 0
#             normal_arr[i][j] = 0
#             disable_arr[i][j] = 0
#         elif arr[j] == 'G' : # 초록 : 정상 = 1, 비정상 = 0
#             normal_arr[i][j] = 1
#             disable_arr[i][j] = 0
#         elif arr[j] == 'B' : # 파랑 : 정상 = 2, 비정상 = 2
#             normal_arr[i][j] = 2
#             disable_arr[i][j] = 2

# normal_count = 0
# for i in range(n) :
#     for j in range(n) :
#         if normal_visited[i][j] == False :
#             normal_count += 1
#             normal_bfs(i, j, normal_arr[i][j])

# disable_count = 0
# for i in range(n) :
#     for j in range(n) :
#         if disable_visited[i][j] == False :
#             disable_count += 1
#             disable_bfs(i, j, disable_arr[i][j])

# print(normal_count, disable_count)


import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y, color) :
    visited[i][j] = True
    q = deque()
    q.append((x, y, color))

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    while q :
        x, y, color = q.popleft()
        
        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue

            if nom[nx][ny] == color and visited[nx][ny] == False :
                visited[nx][ny] = True
                q.append((nx, ny, nom[nx][ny]))

def dis_bfs(x, y, color) :
    q = deque()
    q.append((x, y, color))

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    while q :
        x, y, color = q.popleft()
        
        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue

            if dis[nx][ny] == color and not visited[nx][ny] :
                visited[nx][ny] = True
                q.append((nx, ny, dis[nx][ny]))


n = int(input())
nom = [[0] * n for _ in range(n)]
dis = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n) :
    str = input().strip()
    arr = list(str)

    for j in range(len(arr)) :
        if arr[j] == 'R' : # 빨강 : 정상 = 0, 비정상 = 0
            nom[i][j] = 0
            dis[i][j] = 0
        elif arr[j] == 'G' : # 초록 : 정상 = 1, 비정상 = 0
            nom[i][j] = 1
            dis[i][j] = 0
        elif arr[j] == 'B' : # 파랑 : 정상 = 2, 비정상 = 2
            nom[i][j] = 2
            dis[i][j] = 2

nom_count = 0
for i in range(n) :
    for j in range(n) :
        if visited[i][j] == False :
            bfs(i, j, nom[i][j])
            nom_count += 1

visited = [[False] * n for _ in range(n)]

dis_count = 0
for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            visited[i][j] = True
            dis_bfs(i, j, dis[i][j])
            dis_count += 1

print(nom_count, end = ' ')
print(dis_count)