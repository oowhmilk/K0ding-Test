# 에라토스테네스의 체 알고리즘
# 다수의 자연수에 대하여 소수 여부를판별
# N 보다 작거나 같은 모든 소수를 찾을 때 사용

# 1. 2 부터 N 까지의 모든 자연수를 나열
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은수 i 를 찾기
# 3. 남은 수 중에서 i 의 배수를 모두 제거 (i 는 소수이기 때문에 제거하지 않는다.)
# 4. 더 이상 반복할 수 없을때 까지 2, 3 번 반복

import sys
input = sys.stdin.readline
import math

def check(x) :
    for i in range(2, x) :
        if x % i == 0 :
            return False
    
    return True

n = int(input())

if n == 1 :
    print(0)
    sys.exit()

arr = [True for i in range(n + 1)] # 모든 수가 소수(True) 인 것을 초기화
prime = []

for i in range(2, int(math.sqrt(n)) + 1) : # 2 부터 n의 제곱근까지의 모든 수를 확인
    if arr[i] == True : # i 가 소수인 경우
        j = 2
        while i * j <= n : # i 를 제외한 모든 배수를 False로 바꾸기
            arr[i * j] = False
            j += 1

for i in range(2, n + 1) :
    if arr[i] :
        prime.append(i)

if len(prime) == 1 :
    print(1)
    sys.exit()

left = 0 
right = 1

count = 0
sum = prime[left] + prime[right]

while left < right :
    if sum < n :
        right += 1
        sum += prime[right]

    elif sum == n :
        sum -= prime[left]
        left += 1
        right += 1
        sum += prime[right]
        count += 1

    else :
        sum -= prime[left]
        left += 1

if prime[len(prime) - 1] == n :
    print(count + 1)
else :
    print(count)