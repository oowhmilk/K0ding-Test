import sys
input = sys.stdin.readline

def count_people(mid) :

    count = 0
    for x in arr :
        
        count += int(mid // x)

    return count

n, m = map(int, input().split(' '))

arr = []
for _ in range(n) :
    arr.append(int(input()))

arr.sort()

l = 0
r = m * arr[0]
result = 0

while l <= r :
    mid = int((l + r) // 2)

    count = count_people(mid)
    
    if count < m :
        l = mid + 1
    elif count >= m :
        r = mid - 1
        result = mid

print(result)
