import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

l = 1
r = max(arr)
answer = 0

while l <= r :
    mid = int((l + r) // 2)

    count = 0
    for x in arr :
        if mid <= x :
            count += int(x // mid)

    if n <= count:
        l = mid + 1
        answer = mid
    else :
        r = mid - 1
        
print(answer)
