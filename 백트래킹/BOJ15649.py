import sys
input = sys.stdin.readline

def permutations(n, new_arr) :
    global arr

    if len(new_arr) == n :
        for x in new_arr :
            print(x, end = ' ')
        print()
        return

    for i in range(len(arr)) :
        if not visited[i] :
            visited[i] = True
            permutations(n, new_arr + [arr[i]])
            visited[i] = False
    
n, m = map(int, input().split(' '))
arr = []

for i in range(1, n + 1) :
    arr.append(i)

visited = [False] * (n)
permutations(m, [])