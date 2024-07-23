# 가장 큰 값은 위치를 옮길 필요가 없다
# "뒤에서 부터 볼때" 가장 큰 값부터 내림차순으로 구성된 원소들은 위치를 옮길 필요가 없다

import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n) :
    arr.append(int(input()))

now = n
for i in range(n - 1 , -1, -1) :
    if now == arr[i] :
        now -= 1

print(now)