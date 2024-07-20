# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(100000)

# def dfs(start, value) :
#     global end

#     if start == end :
#         print(value)
#         return

#     for next, add in arr[start] :
#         if visited[next] :
#             continue
#         else :
#             visited[next] = True
#             dfs(next, value + add)



# n, m = map(int, input().split(' '))
# arr = [[] for _ in range(n + 1)]

# for _ in range(n - 1) :
#     x, y, value = map(int, input().split(' '))
#     arr[x].append((y, value))
#     arr[y].append((x, value))

# for _ in range(m) :
#     visited = [False] * (n + 1)
#     start, end = map(int, input().split(' '))

#     visited[start] = True
#     dfs(start, 0)


import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

def dfs(x, count) :
    global end

    if x == end :
        print(count)
        return

    for next, cost in arr[x] :
        if visited[next] :
            continue
        else :
            visited[next] = True
            dfs(next, count = count + cost)


n, m = map(int, input().split(' '))
arr = [[] for _ in range(n + 1)]

for _ in range(n - 1) :
    a, b, cost = map(int, input().split(' '))
    arr[a].append((b, cost))
    arr[b].append((a, cost))


for _ in range(m) :
    start, end = map(int, input().split(' '))
    visited = [False] * (n + 1)

    visited[start] = True
    dfs(start, 0)