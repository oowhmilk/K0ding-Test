import sys
input = sys.stdin.readline

def binary_search(x, left, right) :

    global arr

    while left <= right :
        mid = int((left + right) // 2)

        if arr[mid] == x :
            return True
        elif arr[mid] < x : 
            left = mid + 1
        else :
            right = mid - 1

    return False

n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

m = int(input())
check = list(map(int, input().split(' ')))

for x in check :
    if binary_search(x, 0, len(arr) - 1) :
        print("1")
    else :
        print("0")