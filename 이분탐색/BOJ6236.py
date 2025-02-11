import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

arr =[]
for _ in range(n) :
    arr.append(int(input()))

l = max(arr)
r = sum(arr)

check = True
while l <= r :
    
    mid = (int(l + r) // 2) 
    charge = mid
    count = 1

    for x in arr :
        if charge - x < 0 :
            count += 1
            charge = mid
        charge -= x

    if count > m :
        l = mid + 1
    else :
        r = mid - 1

print(mid)