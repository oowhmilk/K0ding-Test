import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
tree = list(map(int, input().split(' ')))

l = 0
r = max(tree)
finish = False

while l <= r :

    mid = int((l + r) / 2)  
    
    total = 0
    for i in range(n) :
        if mid <= tree[i] :
            total += tree[i] - mid

    if m <= total :
        l = mid + 1
    else :
        r = mid - 1

print(r)