import sys
input = sys.stdin.readline

from collections import deque

def dfs(x, y, count) :
    global ans
    ans = max(ans, count)
    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    for dx, dy in directions :
        nx = x + dx
        ny = y + dy

        if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
            continue

        if alphabet[ord(arr[nx][ny]) - 65] == False:
            alphabet[ord(arr[nx][ny]) - 65] = True
            dfs(nx, ny, count + 1)
            alphabet[ord(arr[nx][ny]) - 65] = False


r, c = map(int, input().split(' '))

arr = []
for i in range(r) :
    str = input()
    arr.append(list(str))

alphabet = [False] * (26)
ans = 1

alphabet[ord(arr[0][0]) - ord('A')] = True

dfs(0, 0, 1)

print(ans)
