import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

def dfs(start, value) :
    global end

    if start == end :
        print(value)
        return

    for next, add in arr[start] :
        if visited[next] :
            continue
        else :
            visited[next] = True
            dfs(next, value + add)



n, m = map(int, input().split(' '))
arr = [[] for _ in range(n + 1)]

for _ in range(n - 1) :
    x, y, value = map(int, input().split(' '))
    arr[x].append((y, value))
    arr[y].append((x, value))

for _ in range(m) :
    visited = [False] * (n + 1)
    start, end = map(int, input().split(' '))

    visited[start] = True
    dfs(start, 0)

