import sys
input = sys.stdin.readline

n = int(input())
arr = [[False] * (101) for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n) :
    x, y, d, g = map(int, input().split(' '))
    current = [d]

    for i in range(g) :
        temp = []
        for j in range(len(current) - 1, -1, -1) :
            temp.append((current[j] + 1) % 4)
        current += temp
    
    arr[x][y] = True
    for i in range(len(current)) :
        x = x + dx[current[i]]
        y = y + dy[current[i]]
        arr[x][y] = True

result = 0
for i in range(100) :
    for j in range(100) :
        if arr[i][j] and arr[i][j + 1] and arr[i + 1][j] and arr[i + 1][j + 1] :
            result += 1

print(result)