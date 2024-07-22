import sys
input = sys.stdin.readline

from collections import deque

a, b = map(int, input().split(' '))

q = deque([])
q.append((a, 0))
visited = set()
found = False

while q :
    x, count = q.popleft()

    if x > int(1e9) :
        continue
    if x == b :
        print(count + 1)
        found = True
        break

    for next in [(x * 2), (10 * x + 1)] :
        if next not in visited :
            q.append((next, count + 1))
            visited.add(next)

if not found :
    print(-1)