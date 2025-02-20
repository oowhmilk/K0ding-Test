from collections import deque
import sys
input = sys.stdin.readline

def bfs(x) :
    q = deque()
    q.append((x, 0))
    visited[x] = True

    count = -1
    while q :
        x, num = q.popleft()

        for next in arr[x] :
            if not visited[next] :
                q.append((next, num + 1))
                visited[next] = True
                count = max(count, num + 1)

    return count

n = int(input())
arr = [[] for _ in range(n + 1)]

while True :
    a, b = map(int, input().split(' '))

    if a == -1 and b == -1 :
        break

    arr[a].append(b)
    arr[b].append(a)

result = [int(1e9)]
for x in range(1, n + 1) :
    visited = [False] * (n + 1)
    count = bfs(x)
    result.append(count)

min_value = min(result)
min_count = 0
for i in range(1, n + 1) :
    if result[i] == min_value :
        min_count += 1

print(min_value, min_count)

for i in range(1, n + 1) :
    if result[i] == min_value :
        print(i, end = ' ')