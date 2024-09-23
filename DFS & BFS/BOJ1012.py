# # import sys 
# # input = sys.stdin.readline

# # sys.setrecursionlimit(100000)

# # def dfs(x, y) :
# #     visited[x][y] = True
# #     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# #     for (dx, dy) in directions :
# #         nx = x + dx
# #         ny = y + dy

# #         if nx < 0 or n <= nx or ny < 0 or m <= ny :
# #             continue
# #         if arr[nx][ny] == 1 and not visited[nx][ny] :
# #             dfs(nx, ny)

# # t = int(input())

# # for _ in range(t) :
# #     m, n, k = map(int, input().split(' '))
# #     arr = [[0] * m for _ in range(n)]
# #     visited = [[False] * m for _ in range(n)]
# #     result = 0

# #     for _ in range(k) :
# #         y, x = map(int, input().split(' '))
# #         arr[x][y] = 1

# #     for i in range(n):
# #         for j in range(m) :
# #             if arr[i][j] == 1 and not visited[i][j] :
# #                 dfs(i , j)
# #                 result += 1

# #     print(result)


# import sys
# from collections import deque
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline

# def bfs(x, y) :
#     q = deque([(x, y)])

#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     while q :
#         x, y = q.popleft()
        
#         for dx, dy in directions :
#             nx = x + dx 
#             ny = y + dy

#             if nx < 0 or n <= nx or ny < 0 or m <= ny :
#                 continue
            
#             if arr[nx][ny] == 1 and not visited[nx][ny] :
#                 q.append((nx, ny))
#                 visited[nx][ny] = True



# for _ in range(int(input())) :
#     m, n, k = map(int, input().split(' '))

#     arr = [[0] * m for _ in range(n)]
#     visited = [[False] * m for _ in range(n)]

#     for _ in range(k) :
#         y, x = map(int, input().split(' '))
#         arr[x][y] = 1

#     count = 0

#     for i in range(n) :
#         for j in range(m) :
#             if arr[i][j] == 1 and not visited[i][j] :
#                 visited[i][j] = True
#                 bfs(i, j)
#                 count += 1

#     print(count)

import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y) :
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    while q :
        x, y = q.popleft()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or m <= ny :
                continue

            if arr[nx][ny] == 1 and not visited[nx][ny] :
                visited[nx][ny] = True
                q.append((nx, ny))

for _ in range(int(input())) :
    m, n, k = map(int, input().split(' '))

    arr = [[0] * m for _ in range(n)]

    for _ in range(k) :
        y, x = map(int, input().split(' '))
        arr[x][y] = 1

    visited = [[False] * m for _ in range(n)]
    count = 0
    for i in range(n) :
        for j in range(m) : 
            if arr[i][j] == 1 and not visited[i][j] :
                bfs(i, j)
                count += 1 
    
    print(count)