import sys
input = sys.stdin.readline

def dfs(x, y) :
    global count

    visited[x][y] = True
    count += 1

    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    for dx, dy in directions : 
        nx = x + dx
        ny = y + dy

        if nx < 0 or n <= nx or ny < 0 or n <= ny :
            continue

        if arr[nx][ny] == 1 and  visited[nx][ny] == False :
            dfs(nx, ny)


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

result = 0
total = []
for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 1 and visited[i][j] == False :
            result += 1
            count = 0
            dfs(i, j)
            total.append(count)

print(result)

total = sorted(total)
for data in total :
    print(data)