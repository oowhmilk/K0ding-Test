from collections import deque
import sys
input = sys.stdin.readline

def bfs(start) :
    q = deque()
    q.append(start)
    visited = [False] * n

    while q :
        x = q.popleft()

        for i in range(n) :
            if not visited[i] and arr[x][i] == 1 :
                q.append(i)
                visited[i] = True
                result[start][i] = 1

n = int(input())

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

result = [[0] * n for _ in range(n)]

for i in range(n) :
    bfs(i)

for i in result:
    print(*i)
