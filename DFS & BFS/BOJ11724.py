import sys
input = sys.stdin.readline

from collections import deque

def bfs(x) :
    q = deque()
    q.append(x)
    visited[x] = True

    while q :
        x = q.popleft()

        for next in arr[x] :
            if not visited[next] :
                q.append(next)
                visited[next] = True

n, m = map(int, input().split(' '))

arr = [[] for _ in range(n + 1)]
for _ in range(m) :
    u, v = map(int, input().split(' '))
    arr[u].append(v)
    arr[v].append(u)

visited = [False] * (n + 1)

count = 0
for i in range(1, n + 1) :
    if not visited[i] :
        bfs(i)
        count += 1

print(count)
