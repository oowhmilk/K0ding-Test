# import sys
# input = sys.stdin.readline

# from collections import deque

        
# def bfs() :
#     q = deque([1])

#     while q :
#         v = q.popleft()
#         if v == n :
#             return arr[v]
#         for next in v * 3, v * 2, v + 1 :
#             if 0 <= next < 100001 and not arr[next] :
#                 arr[next] = arr[v] + 1
#                 q.append(next)

# n = int(input())
# arr = [0] * (200001)
# print(bfs())

n = int(input())
arr = [0] * (int(1e6) + 1)

for i in range(2, n + 1) :
    arr[i] = arr[i - 1] + 1
    if i % 3 == 0 :
        arr[i] = min(arr[i], arr[i // 3] + 1)
    if i % 2 == 0 :
        arr[i] = min(arr[i], arr[i // 2] + 1)

print(arr[n])