# 가장 긴 공통 부분 수열 ( LCS )
# 두 수열을 X, Y 
# 
# D[i][j] = X[0..i] 와 Y[0..j] 의 공통 부분 수열의 최대 길이
# 두 문자열의 길이를 조금씩 늘려 가며 확인하여, 공통 부분 수열의 최대길이를 갱신한다

# 점화식
# D[i][j] = D[i - 1][j - 1] + 1 if X[j] = Y[j]
# D[i][j] = Max( D[i][j - 1], D[i - 1][j] ) if X[j] != Y[j]


# x = input()
# y = input()

# dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
# for i in range(1, len(x) + 1):
#     for j in range(1, len(y) + 1):
#         if x[i - 1] == y[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

# print(dp[len(x)][len(y)])


# x = input()
# y = input()

# dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)] 
# for i in range(1, len(x) + 1) :
#     for j in range(1, len(y) + 1) :
#         if x[i - 1] == y[j - 1] :
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else :
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# print(dp[len(x)][len(y)])

import sys
input = sys.stdin.readline

x = input().strip()
y = input().strip()

dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

for i in range(1, len(x) + 1) :
    for j in range(1, len(y) + 1) :
        if x[i - 1] == y[j - 1] :
            dp[i][j]= dp[i - 1][j - 1] + 1
        else :
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(x)][len(y)])