import sys
input = sys.stdin.readline

n = int(input())

x, y = n // 2, n // 2
arr = [[0] * n for _ in range(n)]
arr[x][y] = 1

dir = -1
step = 1
num = 2

while 1 :
    if x == 0 and y == 0 :
        break

    for _ in range(step) :
        if x == 0 and y == 0 :
            break
        arr[x + dir][y] = num
        x = x + dir
        num += 1

    dir *= -1

    for _ in range(step) :
        if x == 0 and y == 0 :
            break
        arr[x][y + dir] = num
        y = y + dir
        num += 1

    step += 1

check = int(input())
result_x = 0
result_y = 0

for i in range(n) :
    for j in range(n) :
        if arr[i][j] == check :
            result_x = i + 1
            result_y = j + 1

        print(arr[i][j], end = ' ')
    print()

print(result_x, result_y)