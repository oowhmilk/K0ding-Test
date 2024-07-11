import sys
input = sys.stdin.readline

n = int(input())
arr = []

arr.append((0, 0, 0, 0))
for i in range(1, n + 1) :
    a, h, w = map(int, input().split(' ')) # a : 넓이, h : 높이, w : 무게
    arr.append((i, a, h, w))

arr.sort(key = lambda x : x[3]) # 무게 기준 sort


dp = [0] * (n + 1)

for i in range(1, n + 1) :
    for j in range(0, i) :
        if arr[i][1] > arr[j][1] :# 넓이 비교
            dp[i] = max(dp[i], dp[j] + arr[i][2]) 

max_value = max(dp)
index = n
result = []

while index != 0 :
    if max_value == dp[index] :
        result.append(arr[index][0])
        max_value -= arr[index][2]
    index -= 1
result.reverse()

print(len(result))
[print(i) for i in result]


import sys
input = sys.stdin.readline

n = int(input())
arr = []

arr.append((0, 0, 0, 0))
for i in range(1, n + 1) :
    a, h, w = map(int, input().split(' ')) # a : 넓이, h : 높이, w : 무게
    arr.append((i, a, h, w))

arr.sort(key = lambda x : x[3]) # 무게 기준 sort

dp = [0] * (n + 1)

for i in range(1, n + 1) :
    for j in range(i) :
        if arr[j][1] < arr[i][1] :
            dp[i] = max(dp[i], arr[i][2] + dp[j])

max_value = max(dp)
index = n
result = []

while index != 0 :
    if max_value == dp[index] :
        result.append(arr[index][0])
        max_value -= arr[index][2]
    index -= 1
result.reverse()

print(len(result))
[print(i) for i in result]