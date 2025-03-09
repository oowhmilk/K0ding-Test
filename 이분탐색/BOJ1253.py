import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

count = 0
for i in range(n) :

    l = 0
    r = len(arr) - 1

    while l < r:
        check = arr[l] + arr[r]
    
        if check == arr[i] :
            if l == i :
                l += 1
            elif r == i :
                r -= 1
            else :
                count += 1
                break
            
        elif check < arr[i] :
            l += 1
        else :
            r -= 1

print(count)
