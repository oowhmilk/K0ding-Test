import sys
input = sys.stdin.readline

n = int(input())

lines = []
for _ in range(n):
    lines.append(tuple(map(int, input().split())))

lines.sort()

left = lines[0][0]
right = lines[0][1]
ans = 0

for i in range(1, n) :
    if right > lines[i][1] :
        continue

    elif lines[i][0] <= right < lines[i][1] :
        right = lines[i][1]

    elif  right < lines[i][0] :
        ans += right - left
        left = lines[i][0]
        right = lines[i][1]

ans += right - left

print(ans)


import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n) :
    x, y = map(int, input().split(' '))
    arr.append((x, y))

arr = sorted(arr)

before_x = arr[0][0]
before_y = arr[0][1]

result = 0
for i in range(1, len(arr)) :
    if arr[i][1] < before_y :
        continue
    elif arr[i][0] <= before_y < arr[i][1]:
        before_y = arr[i][1]
    elif before_y < arr[i][0] : 
        result += (before_y - before_x)
        before_x = arr[i][0]
        before_y = arr[i][1]

result += (before_y - before_x)

print(result)