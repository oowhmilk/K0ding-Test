# import sys
# input = sys.stdin.readline

# def cal(x, y, tex) :
#     temp = graph[x][y]
#     for dx, dy in tex :
#         nx = x + dx
#         ny = y + dy

#         if 0 <= nx <n and 0 <= ny < m :
#             temp += graph[nx][ny]
#         else :
#             return 0
        
#     return temp

# n, m = map(int, input().split(' '))

# graph = []
# for _ in range(n) :
#     graph.append(list(map(int, input().split(' '))))

# arr = [
#     [(0,1), (0,2), (0,3)], [(1,0), (2,0), (3,0)], # 1x4 형태 
#         [(0,1), (1,0), (1,1)], # 2x2형태
#         [(1,0),(1,1),(2,1)], [(0,-1), (1,-1), (1,-2)], # ㄹ자 (회전)
#         [(1,0), (1,-1), (2,-1)],[(0,1), (1,1), (1,2)], # ㄹ자 (대칭)
#         [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], # ㄴ자 (회전)
#         [(0,1),(1,1), (2,1)], [(0,1), (0,2), (-1,2)],
#         [(1,0),(2,0),(2,-1)],[(0,1),(0,2),(1,2)], # ㄴ자 (대칭)
#         [(1,0),(2,0),(0,1)], [(1,0),(1,1),(1,2)],
#         [(1,0),(1,1),(1,-1)], [(1,0),(1,1),(2,0)], # ㅗ자(회전)
#         [(0,-1),(1,0),(0,1)],[(0,1),(-1,1),(1,1)] 
#        ]

# max_value = 0
# for i in range(n) :
#     for j in range(m) :
#         for tex in arr :
#             value = cal(i, j, tex)
#             max_value = max(max_value, value)

# print(max_value)

import sys
input = sys.stdin.readline

def dfs(cnt, temp, lst) :
    global ans

    if cnt == 4 :
        ans = max(ans, temp)
        return
    
    for cx, cy in lst :

        dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        for dx, dy in dir :
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                dfs(cnt + 1, temp + arr[nx][ny], lst + [(nx, ny)])
                visited[nx][ny] = 0

n, m = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

ans = 0
visited = [[0] * m for _ in range(n)]

for i in range(n) :
    for j in range(m) :
        visited[i][j] = 1
        dfs(1, arr[i][j], [(i, j)])

print(ans)