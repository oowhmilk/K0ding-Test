import sys
input = sys.stdin.readline

def rain(d, s) :
    positions = []
    for cloud in clouds :
        x, y = cloud
        dx, dy = dir[d - 1]
        x = (x + dx * s) % n
        y = (y + dy * s) % n
        arr[x][y] += 1
        positions.append((x, y))

    return positions

n, m = map(int, input().split(' '))
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
arr = []

for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

for _ in range(m) :
    d, s = map(int, input().split(' '))
    positions = rain(d, s)

    for position in positions :
        x, y = position
        cnt = 0
        
        for i in range(1, 8, 2) :
            dx, dy = dir[i]
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue
            if arr[nx][ny] >= 1 :
                cnt += 1 

        arr[x][y] += cnt
    
    positions = set(positions)
    clouds = []

    for i in range(n) :
        for j in range(n) :
            if arr[i][j] >= 2 and (i, j) not in positions :
                clouds.append((i, j))
                arr[i][j] -= 2

answer = 0
for row in arr  :
    answer += sum(row)

print(answer)