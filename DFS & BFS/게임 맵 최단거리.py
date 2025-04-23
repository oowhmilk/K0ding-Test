from collections import deque
def solution(maps):
    answer = 0

    def bfs(x, y) :
        q = deque()
        q.append((x, y))
        visited[x][y] = 1

        dir = {(-1, 0), (0, 1), (1, 0), (0, -1)}
        while q :
            x, y = q.popleft()

            for dx, dy in dir :
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


    n = len(maps)
    m = len(maps[0])

    visited = [[0] * m for _ in range(n)]
    bfs(0, 0)

    if visited[n - 1][m - 1] <= 1 :
        answer = -1
    else :
        answer = visited[n - 1][m - 1]

    return answer