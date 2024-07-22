# import sys
# input = sys.stdin.readline

# import heapq

# def bfs(x, y) :
#     q = []
#     heapq.heappush(q, (0, x, y))
#     visited[x][y] = 0

#     dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

#     while q :
#         count, x, y = heapq.heappop(q)

#         for dx, dy in dir :
#             nx = x + dx
#             ny = y + dy

#             if nx < 0 or n <= nx or ny < 0 or n <= ny :
#                 continue
            
#             if visited[nx][ny] == -1 :
#                 if graph[nx][ny] == 0 :
#                     heapq.heappush(q, (count + 1, nx, ny))
#                     visited[nx][ny] = count + 1
#                 else :
#                     heapq.heappush(q, (count, nx, ny))
#                     visited[nx][ny] = count
    
#     print(visited[n - 1][n - 1])
                



# n = int(input())
# visited = [[-1] * n for _ in range(n)]

# graph = [[0] * n for _ in range(n)] 
# for i in range(n):
#     row = input()
#     for j in range(n):
#         graph[i][j] = int(row[j])

# # print(graph)

# bfs(0, 0)


import sys
input = sys.stdin.readline

import heapq

def bfs(x, y) :
    heap = []
    heapq.heappush(heap, (0, x, y))
    visited[x][y] = 0

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    while heap :
        count, x, y = heapq.heappop(heap)

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue

            if visited[nx][ny] == -1 :
                if arr[nx][ny] == 1 :
                    visited[nx][ny] = count
                    heapq.heappush(heap, (count, nx, ny))
                else :
                    visited[nx][ny] = count + 1
                    heapq.heappush(heap, (count + 1, nx, ny))


n = int(input())
arr = [[0] * n for _ in range(n)]
for i in range(n) :
    row = input()
    for j in range(n) :
        arr[i][j] = int(row[j])

visited = [[-1] * n for _ in range(n)]

bfs(0, 0)

print(visited[n - 1][n - 1])