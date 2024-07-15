# DP 
# 한 번 계산한 값은 다시 구하지 않음
# 길이가 짧을 때 만들 수 있는 경우의 수를 사용해서 길 때 경우의 수를 구함
# 특정 list 에 값을 가지고 있다가 그 값을 이용해서 풀기
# memorization
# 인접한 항들 사이의 관계식
# D[i] = ' 수열의 길이가 i 일 때의 경우의 수 '
# 피보나치 수 : 점화식 문제 생각

n = int(input())

dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1) :
    dp[i] = (dp[i - 1] + dp [i - 2]) % 15746

print(dp[n])

n = input()
dp = [0] * (1000001)
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1) :
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])