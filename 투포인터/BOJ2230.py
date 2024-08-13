import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

left = 0
min_value = sys.maxsize

for right in range(n):
    while left < right and arr[right] - arr[left] >= m:
        min_value = min(min_value, arr[right] - arr[left])
        left += 1

print(min_value)
