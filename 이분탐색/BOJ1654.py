import sys
input = sys.stdin.readline

k, n = map(int, input().split(' '))

arr = []
for _ in range(k) :
    arr.append(int(input()))

l = 0
r = max(arr)

while l <= r :
    
    mid = int((l + r) / 2)

    if mid == 0 :
        mid = 1

    total = 0
    for x in arr : 
        total += int(x / mid)
    
    if n <= total :
        l = mid + 1
    else :
        r = mid - 1

print(r)