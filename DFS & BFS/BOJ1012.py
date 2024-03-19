import sys 
input = sys.stdin.readline

sys.setrecursionlimit(100000)

def dfs(x, y) :
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for (dx, dy) in directions :
        nx = x + dx
        ny = y + dy

        if nx < 0 or n <= nx or ny < 0 or m <= ny :
            continue
        if arr[nx][ny] == 1 and not visited[nx][ny] :
            dfs(nx, ny)

t = int(input())

for _ in range(t) :
    m, n, k = map(int, input().split(' '))
    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    result = 0

    for _ in range(k) :
        y, x = map(int, input().split(' '))
        arr[x][y] = 1

    for i in range(n):
        for j in range(m) :
            if arr[i][j] == 1 and not visited[i][j] :
                dfs(i , j)
                result += 1

    print(result)