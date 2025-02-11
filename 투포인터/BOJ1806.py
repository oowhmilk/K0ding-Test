import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

for x in arr :
    if m <= x :
        print(1)
        sys.exit()

l = 0
r = 1
sum = arr[l] + arr[r]
min_size = int(1e9)

while l < r and r < len(arr) - 1 :
    if sum < m :
        r += 1
        sum += arr[r]
    else :
        min_size = min(min_size, r - l + 1)
        l += 1

        if l == r :
            r += 1
            sum -= arr[l - 1]
            sum += arr[r]
        else :
            sum -= arr[l - 1]

while l < r :
    if sum < m :
        break
    else :
        min_size = min(min_size, r - l + 1)
        l += 1
        sum -= arr[l - 1]

if min_size == int(1e9) :
    print(0)
else :
    print(min_size)