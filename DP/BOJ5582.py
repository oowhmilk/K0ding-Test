import sys
input = sys.stdin.readline

x = input().strip()
y = input().strip()

dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

answer = 0
for i in range(1, len(x) + 1) :
    for j in range(1, len(y) + 1) :
        if x[i - 1] == y[j - 1] :
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])

print(answer)