# import sys
# input = sys.stdin.readline

# ans = []

# for _ in range(int(input())) :
#     n = int(input())
#     arr = list(map(int, input().split(' ')))
#     arr = sorted(arr)

#     result = [0] * (len(arr))
#     left = 0
#     right = len(arr) - 1

#     for i in range(n) :
#         if right < left :
#             break

#         if i % 2 == 0 :
#             result[left] = arr[i]
#             left += 1
#         else : 
#             result[right] = arr[i]
#             right -= 1

#     dif = 0
#     for i in range(len(result) - 1) :
#         dif = max(dif, abs(result[i] - result[i + 1]))

#     ans.append(dif)

# for data in ans :
#     print(data)


import sys
input = sys.stdin.readline

import heapq

for _ in range(int(input())) :
    n = int(input())
    arr = list(map(int, input().split(' ')))

    arr.sort(reverse=True)

    result = [0] * n
    result[n // 2] = arr[0]

    for i in range(1, n) :
        if i % 2 == 0 :
            result[n // 2 - i // 2 - 1] = arr[i]
        else :
            result[n // 2 + i // 2] = arr[i]

    max_dif = 0
    for i in range(n) :
        dif = abs(result[i] - result[(i + 1) % n])
        max_dif = max(max_dif, dif)

    print(max_dif)


import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    arr = list(map(int, input().split(' ')))
    arr.sort()

    max_dif = 0
    for i in range(n - 2) :
        dif = abs(arr[i] - arr[i + 2])
        max_dif = max(max_dif, dif)

    print(max_dif)