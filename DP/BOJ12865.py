# 배낭 문제
# 배낭을 가능한 배낭 무게 * 경우의 수 로 초기화
# 경우 마다 들어오는 배낭의 무게 까지는 이전의 값 그대로 가져오기
# 배낭 무게 보다 무거운 경우 : 덧셈 이용해서 최댓 값인 배낭을 저장

n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight, value = map(int, input().split())
    for j in range(1, k + 1):
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])