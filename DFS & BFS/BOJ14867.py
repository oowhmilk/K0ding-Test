import sys
input = sys.stdin.readline

from collections import deque

a, b, end_a, end_b = map(int, input().split(' '))

q = deque([])
q.append((0, 0, 0))
visited = set()
found = False

while q :
    x, y, count = q.popleft()

    if x == end_a and y == end_b :
        found = True
        print(count)
        break

    for i in range(6) :
        if i == 0 : # fill a
            next_x = a
            next_y = y
        elif i == 1 : # fill b
            next_x = x
            next_y = b
        elif i == 2 : # from x to y
            if x + y > b :
                next_x = x - (b - y)
                next_y = b
            else :
                next_x = 0
                next_y = x + y
        elif i == 3 : # from y to x
            if x + y > a :
                next_x = a
                next_y = y - (a - x)
            else :
                next_x = x + y
                next_y = 0
        elif i == 4 : # empty a
            next_x = 0
            next_y = y
        elif i == 5 : # empty b
            next_x = x
            next_y = 0

        if (next_x, next_y) not in visited :
            visited.add((next_x, next_y))
            q.append((next_x, next_y, count + 1))

if not found :
    print(-1)
        