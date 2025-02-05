from collections import deque
import sys
input = sys.stdin.readline

def dfs(x) :
    q = deque()
    q.append(x)
    visited[x] = True

    while q :
        x = q.popleft()
        for next in arr[x] :
            if not visited[next] :
                visited[next] = True
                q.append(next)

for _ in range(int(input())) :
    n = int(input())
    fig = list(map(int, input().split(' ')))

    arr = [[] for _ in range(n + 1)]
    for i in range(n) :
        arr[i + 1].append(fig[i])

    visited = [False] * (n + 1)
    count = 0
    for i in range(1, n + 1) :
        if not visited[i] :
            count += 1
            dfs(i)

    print(count)