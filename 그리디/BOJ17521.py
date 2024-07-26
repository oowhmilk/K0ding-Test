# 다음 날짜에 가겨이 오른다면 사기
# 두 인접한 날짜의 차이만 고려해서 다음 날이 오르면 해당 날에 다 사고 다음날에 파는 생각

import sys
input = sys.stdin.readline

n, w = map(int, input().split(' '))
arr = []

for _ in range(n) :
    arr.append(int(input()))

for i in range(n - 1) :
    if arr[i] < arr[i + 1] :
        cnt = 2 // arr[i]
        w += cnt * (arr[i + 1] - arr[i])

print(w)