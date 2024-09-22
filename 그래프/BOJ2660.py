import sys
input = sys.stdin.readline
from collections import deque

def bfs(x) :
    q = deque()
    q.append(x)
    visited[x] = True

    while q :
        x = q.popleft()

        for y in arr[x] :
            if not visited[y] :
                dist[y] = dist[x] + 1
                visited[y] = True
                q.append(y)


n = int(input())

arr = [[] for _ in range(n + 1)]

while 1 :
    x, y = map(int, input().split(' '))

    if x == -1 and y == -1 :
        break
    
    arr[x].append(y)
    arr[y].append(x)

result = []
min_value = int(1e9)

for x in range(1, n + 1) :

    visited = [False] * (n + 1)
    dist = [0] * (n + 1)
    bfs(x)

    if max(dist) < min_value :
        min_value = max(dist)
        result = []
        result.append(x)

    elif max(dist) == min_value :
        result.append(x)

print(min_value, len(result))
for x in result :
    print(x, end = ' ')