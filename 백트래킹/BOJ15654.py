import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()

def products(n, new_arr) :
    global arr

    if len(new_arr) == n :
        for x in new_arr :
            print(x, end = ' ')
        print()
        return
    
    for i in range(len(arr)) :
        if not visited[i] :
            visited[i] = True
            products(n, new_arr + [arr[i]])
            visited[i] = False

visited = [False] * (n)
products(m, [])
