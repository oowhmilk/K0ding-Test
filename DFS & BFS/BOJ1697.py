# import sys
# input = sys.stdin.readline

# from collections import deque

# def bfs(n) :
#     deq = deque([n])

#     while deq :
#         v = deq.popleft()

#         if v == k :
#             return array[v]
#         for next in (v - 1, v + 1, v * 2) :
#             if 0 <= next < 100001 and not array[next] :
#                 array[next] = array[v] + 1
#                 deq.append(next)


# n, k = map(int, input().split(' '))

# array = [0] * (2000000 + 1)

# print(bfs(n))

import sys
input = sys.stdin.readline

from collections import deque

def bfs(n) :
    q = deque([n])

    while q :
        v = q.popleft()
        if v == k :
            return arr[v]
        for next in v - 1, v + 1, v * 2 :
            if 0 <= next < 100001 and not arr[next] :
                arr[next] = arr[v] + 1
                q.append(next)


n, k = map(int, input().split(' '))
arr = [0] * (200001)
print(bfs(n))