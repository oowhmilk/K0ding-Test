import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

command_arr = list(map(int, input().split(' ')))

dice = [0] * 6

dir = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
for command in command_arr :

    dx, dy = dir[command]

    nx = x + dx
    ny = y + dy

    if 0 <= nx < n and 0 <= ny < m :
        east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

        if command == 1 :
            dice[0], dice[1], dice[4], dice[5] = down, up, east, west
        elif command == 2 :
            dice[0], dice[1], dice[4], dice[5] = up, down, west, east
        elif command == 3 :
            dice[2], dice[3], dice[4], dice[5] = up, down, north, south
        elif command == 4 :
            dice[2], dice[3], dice[4], dice[5] = down, up, south, north

        if arr[nx][ny] == 0 :
            arr[nx][ny] = dice[5]
        else :
            dice[5] = arr[nx][ny] 
            arr[nx][ny] = 0

        x = nx
        y = ny
        print(dice[4])

    else :
        continue
