from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    arr = [[-1] * (102) for _ in range(102)]

    for r in rectangle :
        x1, y1, x2, y2 = r[0] * 2, r[1] * 2, r[2] * 2, r[3] * 2

        for i in range(x1, x2 + 1) :
            for j in range(y1, y2 + 1) :
                if x1 < i < x2 and y1 < j < y2 :
                    arr[i][j] = 0
                elif arr[i][j] != 0 :
                    arr[i][j] = 1

    cx, cy, ix, iy = 2 * characterX, 2 * characterY, 2 * itemX, 2 * itemY

    visited = [[1] * (102) for _ in range(102)]
    q = deque()
    q.append((cx, cy))

    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
    while q : 
        x, y = q.popleft()

        if x == ix and y == iy :
            answer = visited[x][y] // 2
            break

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if 0 <= nx < 102 and 0 <= ny < 102 and arr[nx][ny] == 1 and visited[nx][ny] == 1 :
                visited[nx][ny] += visited[x][y]
                q.append((nx, ny))

    return answer