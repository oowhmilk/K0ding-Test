import sys
input = sys.stdin.readline

max = 0
index = 0
for i in range(5) :
    sum = 0
    arr = list(map(int, input().split()))

    for j in range(len(arr)) :
        sum += arr[j]

    if max < sum :
        max = sum
        index = i

print(index + 1, max)