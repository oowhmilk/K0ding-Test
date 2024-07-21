# import sys
# input = sys.stdin.readline

# from collections import deque

# def dfs(x, y, cnt) :
#     global ans
#     ans = max(ans, cnt)
#     dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

#     for dx, dy in dir :
#         nx = x + dx
#         ny = y + dy

#         if nx < 0 or r <= nx or ny < 0 or c <= ny :
#             continue

#         if not visited[ord(graph[nx][ny]) - 65] :
#             visited[ord(graph[nx][ny]) - 65] = True
#             dfs(nx, ny, cnt + 1)
#             visited[ord(graph[nx][ny]) - 65] = False


# r, c = map(int, input().split(' '))
# graph = []

# for _ in range(r) :
#     graph.append(input())

# visited = [False] * 26

# ans = 1

# visited[ord(graph[0][0]) - ord('A')] = True

# dfs(0, 0, 1)

# print(ans)


import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

def dfs(x, y, cnt) :
    global result
    result = max(cnt, result)
    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    for dx, dy in dir :
        nx = x + dx
        ny = y + dy

        if nx < 0 or r <= nx or ny < 0 or c <= ny :
            continue
        if not visited[ord(arr[nx][ny]) - ord('A')] :
            visited[ord(arr[nx][ny]) - ord('A')] = True
            dfs(nx, ny, cnt + 1)
            visited[ord(arr[nx][ny]) - ord('A')] = False


r, c = map(int, input().split(' '))
arr = []
for _ in range(r) :
    str = input().strip()
    arr.append(list(str))

visited = [False] * 26
visited[ord(arr[0][0]) - ord('A')] = True

result = 1
dfs(0, 0, 1)

print(result)