# from collections import deque

# def bfs(v) :
#     deq = deque([v])
#     visited = [False] * (n + 1)
#     visited[v] = True
#     count = 1
#     while deq :
#         v = deq.popleft()
#         for e in arr[v] :
#             if not (visited[e]) :
#                 deq.append(e)
#                 visited[e] = True
#                 count += 1

#     return count

# n, m = map(int, input().split(' ')) 
# arr = [[] for _ in range(n + 1)]

# for _ in range(m) :
#     y, x = map(int, input().split(' '))
#     arr[x].append(y)


# result = []
# max_value = -1

# for i in range(1, n + 1) :
#     c = bfs(i)
#     if c > max_value :
#         result = [i]
#         max_value = c        
#     elif c == max_value : 
#         result.append(i)
#         max_value = c

# for e in result :
#     print(e, end = ' ')


import sys
from collections import deque

input = sys.stdin.readline

def bfs(v) :
    q = deque([v])
    visited[v] = True
    count = 1

    while q :
        v = q.popleft()

        for e in arr[v] :
            if not visited[e] :
                q.append(e)
                visited[e] = True
                count += 1

    return count


n, m = map(int, input().split(' '))

arr = [[] for _ in range(n + 1)]

for _ in range(m) :
    a, b = map(int, input().split(' '))
    arr[b].append(a)

result = []
max_value = -1

for i in range(1, n + 1) :
    visited = [False] * (n + 1)
    c = bfs(i)
    if c > max_value :
        result = [i]
        max_value = c
    elif c == max_value :
        result.append(i)

for i in result :
    print(i, end = ' ')
