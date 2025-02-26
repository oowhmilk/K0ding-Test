from collections import deque
import sys
input = sys.stdin.readline

def bfs(x) :
    q = deque()
    q.append(x)
    visited[x] = 0

    while q :
        x = q.popleft()

        for next in arr[x] :
            if visited[next] == -1 :
                q.append(next)
                visited[next] = visited[x] + 1


n, m = map(int, input().split(' '))

arr = [[] for _ in range(n + 1)]
for _ in range(m) :
    a, b = map(int, input().split(' '))

    arr[a].append(b)
    arr[b].append(a)

result = [int(1e9)] * (n + 1)
for x in range(1, n + 1) :
    visited = [-1] * (n + 1)
    bfs(x)
    result[x] = sum(visited) + 1

min_value = int(1e9)
min_result = 0
for i in range(1, n + 1) :
    if min_value > result[i] :
        min_value = result[i]
        min_result = i

print(min_result)