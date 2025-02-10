from collections import deque
import sys
input = sys.stdin.readline

def bfs(x) :
    q = deque()
    q.append((x, 0))
    visited[x] = True

    while q :
        x, count = q.popleft()

        for next in arr[x] :
            if not visited[next] and count < 2 :
                visited[next] = True
                q.append((next, count + 1))
    

n = int(input())

arr = [[] for _ in range(n + 1)]
for _ in range(int(input())) :
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n + 1)

bfs(1)

count = 0
for i in range(2, n + 1) :
    if visited[i] :
        count += 1

print(count)