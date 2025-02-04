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

n = int(input())

arr = [[] for _ in range(n + 1)]
for _ in range(int(input())) :
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n + 1)
bfs(1)

count = 0
for i in range(1, n + 1) :
    if not visited[i] :
        count += 1

print(n - 1 - count)