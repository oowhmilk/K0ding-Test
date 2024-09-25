import sys
input = sys.stdin.readline

def combinations_with_replacement(m, new_arr, i) :
    global arr

    if len(new_arr) == m :
        for x in new_arr :
            print(x, end = ' ')
        print()
        return
    
    for x in range(i, len(arr)) :
        combinations_with_replacement(m, new_arr + [arr[x]], x)

n, m = map(int, input().split(' '))
arr = [i for i in range(1, n + 1)]

combinations_with_replacement(m, [], 0)