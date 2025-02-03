from collections import deque
import sys
input = sys.stdin.readline

def dfs(start) :
    visited[start] = True
    print(start, end = ' ')

    for x in arr[start] :
        if not visited[x] :
            dfs(x)


def bfs(start) :
    q = deque()
    q.append(start)
    visited[start] = True

    while q :
        v = q.popleft()
        print(v, end = ' ')
        
        for x in arr[v] :
            if not visited[x] :
                q.append(x)
                visited[x] = True

n, m, v = map(int, input().split(' '))
arr = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

for e in arr :
    e.sort()

visited = [False] * (n + 1)
dfs(v)

print()

visited = [False] * (n + 1)
bfs(v)