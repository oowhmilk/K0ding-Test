import sys
input = sys.stdin.readline

def rain_move(rain, rain_dir, count) :
    moved_rain = []

    dx, dy = dir[rain_dir]
    for x, y in rain :
        nx = (x + (dx * count) + n) % n
        ny = (y + (dy * count) + n) % n

        moved_rain.append((nx, ny))

    return moved_rain

def rain_magic(x, y) :
    count = 0

    cross_dir = {(-1, -1), (-1, 1), (1, 1), (1, -1)}
    for dx, dy in cross_dir :
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0 :
            count += 1

    return count


n, m = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

rain = [(n - 1, 0), (n - 1, 1),(n - 2, 0), (n - 2, 1)]
dir = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
for _ in range(m) :
    d, s = map(int, input().split(' '))

    # 비구름 이동
    moved_rain = rain_move(rain, d, s)

    # 물의 양 증가
    for x, y in moved_rain :
        arr[x][y] += 1

    # moved_rain 에서 각 정점마다 대각선 값 확인
    for x, y in moved_rain :
        count = rain_magic(x, y)
        arr[x][y] += count

    # 구름 만들기 
    rain = []
    for i in range(n) :
        for j in range(n) :
            if 2 <= arr[i][j] and (i, j) not in moved_rain :
                rain.append((i, j))
                arr[i][j] -= 2

answer = 0
for i in range(n) :
    for j in range(n) :
        answer += arr[i][j]

print(answer)