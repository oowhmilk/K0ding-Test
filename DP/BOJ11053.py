# 가장 긴 증가하는 부분 수열 ( LIS )
# dp[i] = arr[i] 를 마지막 원소로 가지는 부분 수열의 최대 길이
# 모든 0 <= j < i 에 대하여 , dp[i] = max(dp[i], dp[j] + 1) if arr[j] < arr[i]
# 확인하는 인덱스 기준 이전 인덱스 값들을 확인하면서 확인하는 인덱스 값이 더 클 경우에 이전 인덱스 값마다 + 1 을 하고 비교하기
# 결국 DP 문제이기 때문에 이전 값들을 사용할 생각을 하면서 값을 구해야한다. 

# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split(' ')))

# dp = [1] * n

# for i in range(n) :
#     for j in range(i) :
#         if arr[j] < arr[i] :
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))


# n = int(input())
# arr = list(map(int, input().split(' ')))

# dp = [1] * n

# for i in range(n) :
#     for j in range(n) :
#         if arr[i] < arr[j] :
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))

dp = [1] * n

for i in range(n) :
    for j in range(n) :
        if arr[i] < arr[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))