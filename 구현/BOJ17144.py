import sys
input = sys.stdin.readline

def dust(x, y) :

    dir ={(-1, 0), (1, 0), (0, -1), (0, 1)}
    count = 0

    for dx, dy in dir :
        nx = x + dx
        ny = y + dy

        if nx < 0 or r <= nx or ny < 0 or c <= ny :
            continue
        
        if arr[nx][ny] != -1 : # 공기청정기가 아닌 경우 
            new_arr[nx][ny] += int(arr[x][y] / 5)
            count += 1

    new_arr[x][y] += arr[x][y] - (int(arr[x][y] / 5) * count)


def cycle() :
    global arr

    x, y = up_position
    up(arr, x - 1, y, 'U')
    arr[x][y + 1] = 0

    x, y = down_position
    down(arr, x + 1, y, 'D')
    arr[x][y + 1] = 0


def up(arr, x, y, direction) :
    
    if direction == 'U' :
        nx, ny = x - 1, y
        if nx == -1 :
            direction = 'R'

    if direction == 'R' :
        nx, ny = x, y + 1 
        if ny == c :
            direction = 'D'

    if direction == 'D' :
        nx, ny = x + 1, y
        if nx == up_position[0] + 1 :
            direction = 'L'

    if direction == 'L' :
        nx, ny = x, y - 1

    if (nx, ny) != up_position :
        arr[x][y] = arr[nx][ny]
        up(arr, nx, ny, direction)


def down(arr, x, y, direction) :
    
    if direction == 'D' :
        nx, ny = x + 1, y
        if nx == r :
            direction = 'R'

    if direction == 'R' :
        nx, ny = x, y + 1 
        if ny == c :
            direction = 'U'

    if direction == 'U' :
        nx, ny = x - 1, y
        if nx == down_position[0] - 1 :
            direction = 'L'

    if direction == 'L' :
        nx, ny = x, y - 1

    if (nx, ny) != down_position :
        arr[x][y] = arr[nx][ny]
        down(arr, nx, ny, direction)


r, c, t = map(int, input().split(' '))
arr = []

for _ in range(r) :
    arr.append(list(map(int, input().split(' '))))

for i in range(r) :
        for j in range(c) :
            if arr[i][j] == -1 :
                up_position = (i - 1, j)
                down_position = (i, j)

for _ in range(t) :
    new_arr = [[0] * c for _ in range(r)]
    for i in range(r) :
        for j in range(c) :
            if arr[i][j] == -1 :
                new_arr[i][j] = -1

            if 0 < arr[i][j] : # 미세먼지가 존재할 경우
                dust(i, j)

    arr = new_arr
    cycle()

result = 0
for i in range(r) :
    for j in range(c) :
        if arr[i][j] != -1 :
            result += arr[i][j]

print(result)