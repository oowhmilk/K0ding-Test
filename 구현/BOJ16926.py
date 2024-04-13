import sys
input = sys.stdin.readline

n, m ,r = map(int, input().split(' '))

arr = []
for i in range(n) :
    arr.append(list(map(int, input().split(' '))))

for _ in range(r) :
    for i in range(min(n, m) // 2) :
        x, y = i, i
        value = arr[x][y]

        for j in range(i + 1, n - i) :
            x = j
            temp = arr[x][y]
            arr[x][y] = value
            value = temp

        for j in range(i + 1, m - i) :
            y = j
            temp = arr[x][y]
            arr[x][y] = value
            value = temp

        for j in range(i + 1, n - i) :
            x = n - j - 1
            temp = arr[x][y]
            arr[x][y] = value
            value = temp

        for j in range(i + 1, m - i) :
            y = m - j - 1
            temp = arr[x][y]
            arr[x][y] = value
            value = temp


for i in range(n) :
    for j in range(m) :
        print(arr[i][j], end = ' ')
    print()