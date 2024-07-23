# 각 날짜별로, 뒤에 오는 날짜의 주가 중에서 최댓값을 저장
# 각 날짜를 기준으로 "이후 날짜" 의 최댓값 구하기
# 최댓값 구하는 법 : 배열 맨 뒤에서 부터 하나씩 확인하면서 더 큰 값을 만날때까지 저장하다가 큰 값 만나면 값 바꿔서 저장

import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    arr = list(map(int, input().split(' ')))

    max_value = arr[n - 1]
    target = [0] * n

    for i in range(n - 1, -1, -1) :
        if arr[i] < max_value :
            target[i] = max_value
        else : 
            max_value = arr[i]
            target[i] = max_value
    
    result = 0
    for i in range(n) :
        result += max(0, target[i] - arr[i])
        
    print(result)