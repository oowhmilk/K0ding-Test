from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, count) : 
    q = deque()
    q.append((x, count))
    visited[x] = True

    while q :
        x, count = q.popleft()

        if count == 2 :
            break

        for y in arr[x] :
            if not visited[y] :
                q.append((y, count + 1))
                visited[y] = True

n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]
for _ in range(m) :
    a, b = map(int, input().split(' '))
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n + 1)
bfs(1, 0)

result = -1
for i in range(len(visited)) : 
    if visited[i] == True :
        result += 1

print(result)