import sys
input = sys.stdin.readline

def products(n, new_arr) :
    global arr

    if len(new_arr) == n :
        for x in new_arr :
            print(x, end = ' ')
        print()
        return

    for i in range(len(arr)) :
        products(n, new_arr + [arr[i]])


n, m = map(int, input().split(' '))

arr = []
for i in range(1, n + 1) :
    arr.append(i)

# 중복 순열
products(m, [])