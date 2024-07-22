import sys
input = sys.stdin.readline

from collections import deque

s, t = map(int, input().split(' '))

if s == t :
    print(0)
    sys.exit()

result = ""

q = deque([])
q.append((s, result))
visited = set()
found = False

while q :
    x, result = q.popleft()

    if x == t :
        found = True
        print(result)
        break
    
    if x > int(1e9) :
        continue

    for opr in ['*', '+', '-', '/'] :
        if opr == '*' :
            next = x * x
        elif opr == '+' :
            next = x + x
        elif opr == '-' :
            next = x - x
        elif opr == '/' :
            if x != 0 :
                next = x / x      

        if next not in visited :
            visited.add(next)
            q.append((next, result + opr))

if not found :
    print(-1)