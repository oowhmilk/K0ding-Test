import sys
input = sys.stdin.readline

h, w = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

total = 0
for i in range(1, w - 1) :
    left_max = max(arr[:i])
    right_max = max(arr[i + 1 :])

    min_value = min(left_max, right_max)

    if min_value > arr[i] :
        total += min_value - arr[i]

print(total)