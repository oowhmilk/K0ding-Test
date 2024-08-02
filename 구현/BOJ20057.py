import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

left = [(-2, 0, 0.02), (-1, -1, 0.10), (-1, 0, 0.07), 
        (-1, 1, 0.01), (0, -2, 0.05), (1, -1, 0.10),
        (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)]

down = [(-y, x, val) for x, y, val in left]
right = [(x, -y, val) for x, y, val in left]
up = [(y, x, val) for x, y, val in left]
ratio = [left, down, right, up]

def move() :
    global x, y, direction, turned, moved, target
    if moved == target :
        moved = 0
        turned += 1
        direction = (direction + 1) % 4

    if turned == 2 :
        turned = 0
        target += 1

    x = x + dx[direction]
    y = y + dy[direction]
    moved += 1

n = int(input())
arr = []

for i in range(n) :
    arr.append(list(map(int, input().split(' '))))

x = n // 2
y = n // 2

direction = 0
turned = 0
moved = 0
target = 1
result = 0 
cnt = 1

while cnt < n * n :
    move()
    remain = arr[x][y]
    for i in range(9) :
        nx, ny, percentage = ratio[direction][i]
        nx += x 
        ny += y
        current = int(arr[x][y] * percentage)

        if nx < 0 or n <= nx or ny < 0 or n <= ny :
            result += current
        else :
            arr[nx][ny] += current
        
        remain -= current

    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or n <= nx or ny < 0 or n <= ny :
        result += remain
    else :
        arr[nx][ny] += remain

    arr[x][y] = 0
    cnt += 1

print(result)