from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_x, start_y, count) :
    global d
    q = deque()
    q.append((start_x, start_y, count))
    visited[start_x][start_y] = True

    dir = [(-1, 0), (0 ,1), (1, 0), (0, -1)]
    while q :
        x, y, count = q.popleft()

        change = False
        for dx, dy in dir :
            nx = x + dx
            ny = y + dy 

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != 1 :
                change = True

        if change :
            d = ((d - 1)+ 4) % 4
            dx, dy = dir[d]
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != 1 :
                q.append((nx, ny, count + 1))
                visited[nx][ny] = True
            else :
                q.append((x, y, count))

        else :
            dx, dy = dir[(d + 2) % 4]
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1 :
                q.append((nx, ny, count))
            else :
                return count

n, m = map(int, input().split(' '))
robot_x, robot_y, d = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

visited = [[False] * m for _ in range(n)]
result = bfs(robot_x, robot_y, 1)
print(result)