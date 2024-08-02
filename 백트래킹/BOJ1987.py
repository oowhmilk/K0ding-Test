# 백트래킹 할때 이전의 값을 다시 돌아가서 확인해야하기 때문에 
# dfs 를 이용할 경우 재귀함수 이후에 True 를 False 로 바꿔주는게 중요하다
# 
# bfs 를 이용할 경우 기존의 deque 를 사용하는 방식이 아닌 set 을 이용하는 방식
# set 은 집합 자료형으로써 동일한 경우는 한 번만 계산하기 위해 

import sys
input = sys.stdin.readline

def bfs(x, y) :
    global result
    dir = {(-1, 0), (0, -1), (1, 0), (0, 1)}


    q = set()
    q.add((x, y, arr[x][y]))

    while q :
        x, y, step = q.pop()
        result = max(result, len(step))
        
        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if 0 <= nx and nx < r and 0 <= ny and ny < c and arr[nx][ny] not in step :
                q.add((nx, ny, step + arr[nx][ny]))
            

r, c = map(int, input().split(' '))
arr = []
for _ in range(r) :
    arr.append(input())

result = 0
bfs(0, 0)
print(result)


# import sys
# input = sys.stdin.readline

# from collections import deque

# def dfs(x, y, count) :
#     global ans
#     ans = max(ans, count)
#     directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
#     for dx, dy in directions :
#         nx = x + dx
#         ny = y + dy

#         if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
#             continue

#         if alphabet[ord(arr[nx][ny]) - 65] == False:
#             alphabet[ord(arr[nx][ny]) - 65] = True
#             dfs(nx, ny, count + 1)
#             alphabet[ord(arr[nx][ny]) - 65] = False


# r, c = map(int, input().split(' '))

# arr = []
# for i in range(r) :
#     str = input()
#     arr.append(list(str))

# alphabet = [False] * (26)
# ans = 1

# alphabet[ord(arr[0][0]) - ord('A')] = True

# dfs(0, 0, 1)

# print(ans)


import sys
input = sys.stdin.readline

def dfs(x, y, count) :
    global ans
    ans = max(ans, count)
    dir = {(-1, 0), (0, -1), (1, 0), (0, 1)}

    for dx, dy in dir :
        nx = x + dx
        ny = y + dy
    
        if nx < 0 or r <= nx or ny < 0 or c <= ny :
            continue
        if alphabet[ord(arr[nx][ny]) - 65] == False :
            alphabet[ord(arr[nx][ny]) - 65] = True
            dfs(nx, ny, count + 1)
            alphabet[ord(arr[nx][ny]) - 65] = False


r, c = map(int, input().split(' '))

arr = []
for i in range(r) :
    str = input()
    arr.append(list(str))

alphabet = [False] * 26

ans = 1
alphabet[ord(arr[0][0]) - ord('A')] = True
dfs(0, 0, 1)
print(ans)

