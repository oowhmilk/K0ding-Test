import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * 301
for i in range(1, n + 1) :
    arr[i] = int(input())

dp = [0] * 301
dp[1] = arr[1]
dp[2] = arr[2]
dp[3] = max(arr[1] + arr[3], arr[2] + arr[3])

for i in range(4, n + 1) :
    dp[i] = max(dp[i - 3] + dp[i - 1] + dp[i], dp[i - 2] + dp[i])

print(dp[i])