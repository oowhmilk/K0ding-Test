import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
x = int(input())

arr = sorted(arr)

low = 0 
high = len(arr) - 1

result = 0
for i in range(n) :
    if high <= low :
        break

    if arr[low] + arr[high] == x :
        result += 1
        low += 1
        high -= 1
    elif arr[low] + arr[high] > x :
        high -= 1
    elif arr[low] + arr[high] < x :
        low += 1

print(result)