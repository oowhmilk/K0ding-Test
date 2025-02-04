import sys
input = sys.stdin.readline

def binary_search(x) :
    l = 0
    r = len(check) - 1

    while l <= r :
        mid = int((l + r) // 2)

        if check[mid] == x :
            return True
        
        if check[mid] < x :
            l = mid + 1
        elif x < check[mid] :
            r = mid - 1

    return False


n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

dic = {}
for x in arr :
    if x in dic :
        dic[x] += 1
    else :
        dic[x] = 1

check = sorted(dic)

m = int(input())
for x in list(map(int, input().split(' '))) :
    if binary_search(x) :
        print(dic[x], end = ' ')
    else :
        print(0, end = ' ')
