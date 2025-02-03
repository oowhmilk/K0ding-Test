from collections import deque
import sys
input = sys.stdin.readline

def bfs(x) :
    q = deque()
    q.append(x)
    visited[x] = True

    while q :
        x = q.popleft()

        for next in arr[x] :
            if not visited[next] :
                visited[next] = True
                q.append(next)

n, m = map(int, input().split(' '))
arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m) :
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

count = 0
for x in range(1, n + 1) :
    if not visited[x] :
        count += 1
        bfs(x)

print(count)