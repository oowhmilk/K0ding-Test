# import sys
# input = sys.stdin.readline

# from collections import deque

# def dfs(v) :
#     global count
#     visited[v] = True
#     count += 1
#     # print(v, end = '')
#     for e in arr[v] :
#         if not (visited[e]) :
#             dfs(e)

# def bfs(v) :
#     global count
#     deq = deque([v])

#     while deq :
#         v = deq.popleft()
#         if not (visited[v]) :
#             visited[v] = True
#             count += 1
#             # print(v, end = '')
#             for e in arr[v] :
#                 if not (visited[e]) :
#                     deq.append(e)


# n = int(input())
# m = int(input())

# arr = [[] for _ in range(n + 1)]

# for _ in range(m) :
#     x, y = map(int, input().split(' '))
#     arr[x].append(y)
#     arr[y].append(x)

# visited = [False] * (n + 1)
# count = 0
# dfs(1)
# # bfs(1)

# print(count - 1)


import sys
from collections import deque

def bfs(n) :
    global count
    count = 0
    q = deque([n])

    while q :
        v = q.popleft()
        if not visited[v] :
            visited[v] = True
            count += 1

            for x in arr[v] :
                if not visited[x] :
                    q.append(x)


n = int(input())

arr = [[] for _ in range(n + 1)]

for _ in range(int(input())) :
    x, y = map(int, input().split(' '))
    arr[x].append(y)
    arr[y].append(x)
    
count = 0
visited = [False] * (n + 1)
bfs(1)

print(count - 1)