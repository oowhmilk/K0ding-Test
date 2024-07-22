import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]

for i in range(m) :
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

q = deque([])
q.append((1, 0))
visited = [False] * (n + 1)
result = 0

while q :
    x, count = q.popleft()
    visited[x] = True

    for next in arr[x] :
        if not visited[next] and count + 1 < 3:
            visited[next] = True
            q.append((next, count + 1))
            result += 1

print(result)