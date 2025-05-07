from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y) :
    q = deque()
    new = set()
    q.append((x, y))
    visited[x][y] = True

    dir = {(-1, 0), (0, -1), (0, 1), (1, 0)}
    while q :
        x, y = q.popleft()
        new.add((x, y))

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not visited[nx][ny] :
                q.append((nx, ny))
                visited[nx][ny] = True

    return list(new)

def cal(i, j) :
    min_value = int(1e9)
    island_x = island[i]
    island_y = island[j]

    for x in island_x :
        for y in island_y :
            min_value = min(min_value, abs(x[0] - y[0]) + abs(x[1] - y[1]))

    return min_value

n = int(input())

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

island = []

visited = [[False] * n for _ in range(n)]
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 and not visited[i][j] :
            new = bfs(i, j)
            island.append(new)

result = int(1e9)
for i in range(len(island)) :
    for j in range(len(island)) :
        if i != j :
            result = min(result, cal(i, j) - 1)

print(result)