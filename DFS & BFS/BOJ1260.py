# from collections import deque

# def dfs(v) :
#     print(v, end = ' ')
#     visited[v] = True
#     for e in adj[v] :
#         if not (visited[e]) :
#             dfs(e)

# def bfs(v) :
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if not (visited[v]) :
#             visited[v] = True
#             print(v, end = ' ')
#             for e in adj[v] :
#                 if not visited[e]:
#                     q.append(e)

# n, m, v = map(int, input().split(' '))
# adj = [[] for _ in range(n + 1)]

# for _ in range(m) :
#     x, y = map(int, input().split(' '))
#     adj[x].append(y)
#     adj[y].append(x)

# for e in adj :
#     e.sort()

# visited = [False] * (n + 1)
# dfs(v)
# print()
# visited = [False] * (n + 1)
# bfs(v)


# import sys
# from collections import deque

# def dfs(v) :
#     print(v, end = ' ')
#     visited[v] = True
#     for e in adj[v] :
#         if not (visited[e]) :
#             dfs(e)

# def bfs(v) :
#     q = deque([v])
#     while q :
#         v = q.popleft()
#         if not (visited[v]) :
#             visited[v] = True
#             print(v, end = ' ')
#             for e in adj[v] :
#                 if not visited[e] :
#                     q.append(e)

# n, m, v = map(int, input().split(' '))
# adj = [[] for _ in range(n + 1)]

# for _ in range(m) :
#     x, y = map(int, input().split(' '))
#     adj[x].append(y)
#     adj[y].append(x)

# for e in adj :
#     e.sort()

# visited = [False] * (n + 1)
# dfs(v)
# print()
# visited = [False] * (n + 1)
# bfs(v)


# import sys
# input = sys.stdin.readline

# from collections import deque

# def dfs(v) :
#     print(v, end = ' ')
#     visited[v] = True
#     for e in arr[v] :
#         if not visited[e] :
#             dfs(e)

# def bfs(v) :
#     q = deque()
#     q.append(v) 

#     while q :
#         v = q.popleft()
#         if not (visited[v]) :
#             visited[v] = True
#             print(v, end = ' ')

#             for e in arr[v] :
#                 if not visited[e] :
#                     q.append(e)


# n, m, v = map(int, input().split(' '))
# arr = [[] for _ in range(n + 1)]

# for _ in range(m) :
#     x, y = map(int, input().split(' '))
#     arr[x].append(y)
#     arr[y].append(x)

# for e in arr :
#     e.sort()

# visited = [False] * (n + 1)
# dfs(v)
# print()
# visited = [False] * (n + 1)
# bfs(v)


import sys
input = sys.stdin.readline
from collections import deque

def dfs(x) :
    visited[x] = True
    print(x, end = ' ')

    for next in arr[x] :
        if not visited[next] :
            dfs(next)

def bfs(x) :
    visited[x] = True
    q = deque()
    q.append(x)

    while q :
        x = q.popleft()
        print(x, end = ' ')
        
        for next in arr[x] :
            if not visited[next] :
                visited[next] = True
                q.append(next)


n, m, v = map(int, input().split(' '))
arr = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

for e in arr :
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)