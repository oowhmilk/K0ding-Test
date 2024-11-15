from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y, count) :
    global end_x, end_y


    q = deque()
    q.append((start_x, start_y, count))

    dir = {(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)}

    while q : 
        x, y, count = q.popleft()

        if x == end_x and y == end_y :
            return count

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or l <= nx or ny < 0 or l <= ny :
                continue

            if not visited[nx][ny] :
                visited[nx][ny] = True
                q.append((nx, ny, count + 1))


for _ in range(int(input())) :
    l = int(input())
    start_x, start_y = map(int, input().split(' '))
    end_x, end_y = map(int, input().split(' '))

    visited = [[False] * l for _ in range(l)]

    print(bfs(start_x, start_y, 0))