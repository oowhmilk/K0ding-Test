import sys
input = sys.stdin.readline

def binary_search(x) :
    l = 0
    r = len(sorted_arr)

    while l <= r :
        mid = (int(l + r) // 2)

        if sorted_arr[mid] == x :
            return mid
        
        elif sorted_arr[mid] < x :
            l = mid + 1
        else :
            r = mid - 1


n = int(input())
arr = list(map(int, input().split(' ')))
sorted_arr = set(arr)
sorted_arr = sorted(sorted_arr)

for x in arr :
    print(binary_search(x), end = ' ')