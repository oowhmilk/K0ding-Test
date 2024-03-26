import sys
input = sys.stdin.readline

from collections import deque

def bfs(v) :
    visited[v] = True
    deq = deque([v])

    while deq :
        now = deq.popleft()
        count = time[now]

        if now == k :
            return count

        for next in (2 * now, now - 1, now + 1) :
            if next < 0 or 100000 < next :
                continue
            if not visited[next] :
                if next == 2 * now :
                    time[next] = count
                else :
                    time[next] = count + 1
                visited[next] = True
                deq.append(next)

n, k = map(int, input().split(' '))

time = [0] * (100000 + 1)
visited = [False] * (100000 + 1)

print(bfs(n))