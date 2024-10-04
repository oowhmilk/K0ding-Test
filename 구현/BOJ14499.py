import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

command = list(map(int, input().split(' ')))
dice = [0] * 6

dir = [(0, 1), (0, -1), (-1, 0), (1, 0)]

for com in command :
    dx, dy = dir[com - 1]
    nx = x + dx
    ny = y + dy

    if nx < 0 or n <= nx or ny < 0 or m <= ny :
        continue

    east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    if com == 1 :
        dice[0], dice[1], dice[4], dice[5] = down, up, east, west
    elif com == 2 :
        dice[0], dice[1], dice[4], dice[5] = up, down, west, east
    elif com == 3 :
        dice[2], dice[3], dice[4], dice[5] = up, down, north, south
    elif com == 4 :
        dice[2], dice[3], dice[4], dice[5] = down, up, south, north

    if arr[nx][ny] == 0 :
        arr[nx][ny] = dice[5]
    else :
        dice[5] = arr[nx][ny] 
        arr[nx][ny] = 0

    x = nx
    y = ny
    print(dice[4])