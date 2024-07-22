# BFS 로 녹일 위치를 선택하고, 녹이는 과정을 반복 수행
# 치즈 내무의 공간은 치즈 외부 공기와 접촉하지 않은 것 -> 단순히 주변 0 인걸로 판단 불가
# 외부 고기를 정확히 파악하기 위 (0, 0) 의 위치에서 출발

import sys
input = sys.stdin.readline

from collections import deque

def bfs() :
    q = deque([])
    q.append((0, 0))
    visited[0][0] = True

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    while q :
        x, y = q.popleft()
        
        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or m <= ny :
                continue

            if not visited[nx][ny] :
                if arr[nx][ny] >= 1 :
                    arr[nx][ny] += 1
                else :
                    q.append((nx, ny))
                    visited[nx][ny] = True

def melt() :
    finish = True
    for i in range(n) :
        for j in range(m) :
            if arr[i][j] >= 3 :
                arr[i][j] = 0
                finish = False
            elif arr[i][j] == 2 :
                arr[i][j] = 1

    return finish


n, m = map(int, input().split(' '))

arr = [[] for _ in range(n)]
for i in range(n) :
    arr[i] = (list(map(int, input().split(' '))))


result = 0
while 1 :

    visited = [[False] * m for _ in range(n)]
    bfs()

    if melt() :
        print(result)
        break
    else :
        result += 1
