import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
arr = []

for i in range(n) : 
    arr.append(i + 1)

# 조합 구현
def combinations(n, new_arr, c) :
    global arr

    if len(new_arr) == n :
        for i in range(len(new_arr)) :
            print(new_arr[i], end = ' ')
        print()
        return

    for i in range(c, len(arr)) :
        combinations(n, new_arr + [arr[i]], i + 1)

combinations(m, [], 0)
