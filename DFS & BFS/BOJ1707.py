# 이분 그래프 : 노드들을 두 개의 집합으로 분할하여, 같은 집합에 속한 정점끼리 서로 인접하지 않는 그래프
# 정점들을 파란색, 빨간색으로 나누면
# 빨간색 끼리 또는 파란색 끼리는 인접 하면 안된다.

# import sys
# input = sys.stdin.readline

# from collections import deque

# def bfs(v) :
#     q = deque([v])
#     visited[v] = 0

#     while q :
#         x = q.popleft()
#         color = visited[x]

#         for y in graph[x] :
#             if visited[y] == -1 :
#                 visited[y] = (color + 1) % 2
#                 q.append(y)
#             elif visited[y] == 0 :
#                 if color == 0 :
#                     return False
#             else :
#                 if color == 1 :
#                     return False
                
#     return True




# k = int(input())

# for _ in range(k) :
#     V, E = map(int, input().split(' '))

#     graph = [[] for _ in range(V + 1)]
    

#     for _ in range(E) :
#         u, v = map(int, input().split(' '))
#         graph[u].append(v)
#         graph[v].append(u)
        
#     visited = [-1] * (V + 1)

#     cnt = 0
#     for i in range(1, V + 1) :
#         if visited[i] == -1 :
#             check = bfs(i)
#             if check == False :
#                 cnt = 1

#     if cnt == 1 :
#         print("NO")
#     else :
#         print("YES")


import sys
input = sys.stdin.readline

from collections import deque

def bfs(x) :
    q = deque()
    q.append(x)
    visited[x] = 0

    while q :
        x = q.popleft()

        for y in arr[x] :
            if visited[y] == -1 :
                visited[y] = (visited[x] + 1) % 2
                q.append(y)

def is_bipartitie() :
    for x in range(1, v + 1) :
        for y in arr[x] :
            if visited[x] == visited[y] :
                return False
    return True

for _ in range(int(input())) :
    v, e = map(int, input().split(' '))
    arr = [[0] for _ in range(v + 1)]

    for _ in range(e) :
        x, y = map(int, input().split(' '))
        arr[x].append(y)
        arr[y].append(x)

    visited = [-1] * (v + 1)
    for i in range(1, v + 1) :
        if visited[i] == -1 :
            bfs(i)
    
    if is_bipartitie() :
        print("YES")
    else :
        print("NO")

