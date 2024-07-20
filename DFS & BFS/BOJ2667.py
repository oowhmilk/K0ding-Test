# import sys
# input = sys.stdin.readline

# def dfs(x, y) :
#     global count

#     dir = {(-1, 0), (1 , 0), (0, -1), (0, 1)}
#     visited[x][y] = True
#     count += 1

#     for dx, dy in dir :
#         nx = x + dx
#         ny = y + dy

#         if nx < 0 or n <= nx or ny < 0 or n <= ny :
#             continue

#         if arr[nx][ny] == 1 and not visited[nx][ny] :
#             dfs(nx, ny)


# n = int(input())
# arr = [[0] * (n) for _ in range(n)]
# visited = [[False] * (n) for _ in range(n)]

# for i in range(n) :
#     str = input().strip()
#     change = list(str)
#     for j in range(n) :
#         if change[j] == '0' :
#             arr[i][j] = 0
#         else : 
#             arr[i][j] = 1


# result = 0
# total = []
# for i in range(n) :
#     for j in range(n) :
#         if arr[i][j] == 1 and not visited[i][j] :
#             result += 1
#             count = 0
#             dfs(i, j)
#             total.append(count)


# print(result)
# for x in sorted(total) :
#     print(x)


import sys
input = sys.stdin.readline

from collections import deque

def bfs(x, y) :
    global count 
    q = deque([(x, y)])

    dir = {(-1, 0), (0, -1), (1, 0), (0, 1)}
    while q :
        x, y = q.pop()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue
            if arr[nx][ny] == 1 and not visited[nx][ny] :
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1


n = int(input())
arr = [[0] * (n) for _ in range(n)]
visited = [[False] * (n) for _ in range(n)]

for i in range(n) :
    str = input().strip()
    change = list(str)
    for j in range(n) :
        if change[j] == '0' :
            arr[i][j] = 0
        else : 
            arr[i][j] = 1

total = 0
result = []
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 and not visited[i][j] :
            count = 1
            visited[i][j] = True
            bfs(i, j)
            total += 1
            result.append(count)

print(total)
for x in sorted(result) :
    print(x)