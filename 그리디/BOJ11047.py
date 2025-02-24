import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(int(input()))

arr = sorted(arr, reverse = True)

count = 0
for x in arr :
    if 0 < int(k // x) :
        count += int(k // x)
        k = int(k % x)

print(count)