# import sys
# input = sys.stdin.readline

# n, s, m = map(int, input().split(' '))
# arr = list(map(int, input().split(' ')))

# volume = [-1] * (m + 1)
# volume[s] = 0

# for i in range(len(arr)) :
#     last = -1
#     check = []
#     for j in range(len(volume)) :

#         if volume[j] == i :
#             check.append(j)

#     for k in range(len(check)) :
#         if 0 <= check[k] - arr[i]  :
#             volume[check[k] - arr[i]] = i + 1
#         if check[k] + arr[i] <= m :
#             volume[check[k] + arr[i]] = i + 1

# # print(volume)

# result = []
# for i in range(len(volume)) :
#     if volume[i] == n :
#         result.append(i)

# if len(result) == 0:
#     print(-1)
# else : 
#     print(max(result))


# n, s, m = map(int, input().split())
# array = list(map(int, input().split()))

# dp = [[0] * (m + 1) for _ in range(n + 1)]
# dp[0][s] = 1
# for i in range(1, n + 1):
#     for j in range(m + 1):
#         if dp[i - 1][j] == 0:
#             continue
#         if j - array[i - 1] >= 0:
#             dp[i][j - array[i - 1]] = 1
#         if j + array[i - 1] <= m:
#             dp[i][j + array[i - 1]] = 1

# result = -1

# for i in range(m, -1, -1):
#     if dp[n][i] == 1:
#         result = i
#         break

# print(result)

import sys
input = sys.stdin.readline

n, s, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

for i in range(1, n + 1) :
    for j in range(1, m + 1) :
        if dp[i - 1][j] == 0 :
            continue
        if j - arr[i - 1] >= 0 :
            dp[j - arr[i - 1]] = 1
        if j + arr[i - 1] <= m :
            dp[j + arr[i - 1]] = 1

result = -1

for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break

print(result)