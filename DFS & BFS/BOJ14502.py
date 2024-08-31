import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs() :

    global visited
    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    while virus : 
        x, y = virus.popleft()
        visited[x][y] = True

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or m <= ny :
                continue

            if not visited[nx][ny] and arr[nx][ny] == 0 :
                visited[nx][ny] = True
                virus.append((nx, ny))

    count = 0
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] == 0 and not visited[i][j]:
                count += 1

    return count


# def find() :
#     count = 0

#     for i in range(n) :
#         for j in range(m) :
#             if arr[i][j] == 0 and not visited[i][j]:
#                 count += 1

#     return count



n, m = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

zero = []
virus = deque()
for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 0 :
            zero.append((i, j))
        elif arr[i][j] == 2 :
            virus.append((i, j))

result = list(combinations(zero, 3))


max_size = 0
for i in range(len(result)) :
    
    for x, y in result[i] :
        arr[x][y] = 1

    visited = [[False] * m for _ in range(n)]
    virus = deque()
    for j in range(n) :
        for k in range(m) :
            if arr[j][k] == 2 :
                virus.append((j, k))
    count = bfs()

    max_size = max(max_size, count)

    for x, y in result[i] :
        arr[x][y] = 0


print(max_size)    