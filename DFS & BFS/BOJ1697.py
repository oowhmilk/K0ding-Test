import sys
input = sys.stdin.readline

from collections import deque

def bfs(n) :
    deq = deque([n])

    while deq :
        v = deq.popleft()

        if v == k :
            return array[v]
        for next in (v - 1, v + 1, v * 2) :
            if 0 <= next < 100001 and not array[next] :
                array[next] = array[v] + 1
                deq.append(next)


n, k = map(int, input().split(' '))

array = [0] * (2000000 + 1)

print(bfs(n))