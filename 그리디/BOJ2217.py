import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n) :
    arr.append(int(input()))
arr.sort()

max_value = 0
for i in range(n) :
    value = (i + 1) * arr[len(arr) - 1 - i]
    max_value = max(max_value, value)

print(max_value)