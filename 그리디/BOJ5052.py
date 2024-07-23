# 접두어를 형성하는 경우, 정렬된 이후에 인접한 문자열을 봤을 때 접두어 관계
# 오름차순 정렬
# 인접한 두 개의 문자열을 확인해 접두어 관계 확인

import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    arr = []

    for i in range(n) :
        number = input().strip()
        arr.append(number)

    arr.sort()

    result = False
    for i in range(n - 1) :
        if len(arr[i]) < len(arr[i + 1]) :
            if arr[i] == arr[i + 1][:len(arr[i])] :
                result = True
                break

    if result : 
        print("NO")
    else :
        print("YES")