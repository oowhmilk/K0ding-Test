import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

arr = [[] for _ in range(n + 1)]
for _ in range(int(input())) :
    x, y = map(int, input().split(' '))
    arr[x].append(y)
    arr[y].append(x)

visited = [False] * (n + 1)

q = deque()
q.append(1)
visited[1] = True
count = 0

while q :
    x = q.popleft()
    for next in arr[x] :
        if not visited[next] :
            visited[next] = True
            q.append(next)
            count += 1

print(count)