import sys
input = sys.stdin.readline

def put(sticker) :
    r = len(sticker)
    c = len(sticker[0])

    for x in range(n - r + 1) :
        for y in range(m - c + 1) :
            if compare(x, y, r, c, sticker) :
                for sx in range(r):
                    for sy in range(c):
                        arr[x + sx][y + sy] += sticker[sx][sy]
                return True

    return False

def compare(x, y, r, c, sticker) :
    for sx in range(r):
        for sy in range(c):
            if arr[x + sx][y + sy] == sticker[sx][sy] == 1:
                return False
    return True

def rotate(arr):
    return list(map(list, zip(*arr[::-1])))


n, m, k = map(int, input().split(' '))
arr = [[0] * m for _ in range(n)]

stickers = []
for _ in range(k) : 
    r, c = map(int, input().split(' '))

    sticker = []
    for _ in range(r) :
        sticker.append(list(map(int, input().split(' '))))

    stickers.append(sticker)

for sticker in stickers :
    for i in range(4) :
        if put(sticker) :
            break
        sticker = rotate(sticker)

cnt = 0
for x in range(n) :
    for y in range(m) :
        if arr[x][y] != 0 :
            cnt += 1

print(cnt)