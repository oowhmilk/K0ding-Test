import sys
input = sys.stdin.readline

for _ in range(int(input())) :


    arr = input().strip()

    l = 0
    r = len(arr) - 1

    count = 0
    while l < r :
        if arr[l] == arr[r] :
            l += 1
            r -= 1
        else :
            if arr[l + 1 : r + 1] == arr[l + 1 : r + 1][::-1] :
                count = 1
                break
            elif arr[l : r] == arr[l : r][::-1] :
                count = 1
                break
            else :
                count = 2
                break

    print(count)