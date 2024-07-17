# 각 센서를 오름차순 정렬
# 정렬된 센서를 K 개의 영역으로 나누는 것과 같음
# 영역을 나눌때 어떻게 나누냐? 
# 각 센서 간의 거리를 구하고 거리가 큰 것부터 K - 1 개 삭제
# 삭제 이후 남은 거리를 전부 더하면 끝

# import sys
# input = sys.stdin.readline

# n = int(input())
# k = int(input())

# arr = list(map(int, input().split(' ')))
# arr.sort()

# if k >= n :
#     print(0)
#     sys.exit()

# dif = []
# for i in range(len(arr) - 1) :
#     dif.append(arr[i + 1] - arr[i])

# dif.sort(reverse = True)

# for i in range(k - 1) :
#     dif[i] = 0

# print(sum(dif))


import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int, input().split(' ')))

arr.sort()

dif = []

for i in range(len(arr) - 1) :
    dif.append(arr[i + 1] - arr[i])

dif = sorted(dif, reverse=True)

for i in range(k - 1) :
    dif[i] = 0

print(sum(dif))