import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

def rotate(q) :
    size = l[q]
    step_size = 2 ** size

    new_arr = [[0] * (2 ** n) for _ in range(2 ** n)]

    for i in range(0, 2 ** n, step_size) :
        for j in range(0, 2 ** n, step_size) :

            small = [[0] * step_size for _ in range(step_size)]    
            for x in range(i, i + step_size) :
                for y in range(j, j + step_size) :
                    small[x - i][y - j] = arr[x][y]

            small_90 = list(map(list, zip(*small[::-1])))

            for x in range(i, i + step_size) :
                for y in range(j, j + step_size) :
                    new_arr[x][y] = small_90[x - i][y - j]

    return new_arr

def melt() :
    melted = []

    dir = {(-1, 0), (0, 1), (1, 0), (0, -1)}

    for x in range(2 ** n) :
        for y in range(2 ** n) :
            cnt = 0

            for dx, dy in dir :
                nx = x + dx
                ny = y + dy

                if nx < 0 or (2 ** n) <= nx or ny < 0 or (2 ** n) <= ny :
                    continue
                if arr[nx][ny] >= 1 :
                    cnt += 1

            if cnt < 3 :
                melted.append((x, y))

    return melted



n, q = map(int, input().split(' '))
arr = []

for _ in range(2 ** n) :
    arr.append(list(map(int, input().split(' '))))

l = (list(map(int, input().split(' '))))


for i in range(q) :
    arr = rotate(i)

    melted = melt()

    for (x, y) in melted :
        if arr[x][y] >= 1 :
            arr[x][y] -= 1

answer = 0
for row in arr :
    answer += sum(row)

print(answer)


visited = [[False] * (2 ** n) for _ in range(2 ** n)]

def dfs(x, y) :
    result = 1
    dir = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    
    for dx, dy in dir :
        nx = x + dx
        ny = y + dy

        if nx < 0 or (2 ** n) <= nx or ny < 0 or (2 ** n) <= ny :
            continue
        if not visited[nx][ny] and arr[nx][ny] >= 1 :
            visited[nx][ny] = True
            result += dfs(nx, ny)

    return result

max_value = 0
for i in range(2 ** n) :
    for j in range(2 ** n) :
        if not visited[i][j] and arr[i][j] >= 1:
            visited[i][j] = True
            max_value = max(max_value, dfs(i, j))

print(max_value)