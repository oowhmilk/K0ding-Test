import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

def is_cycle(x) :
    visited[x] = True

    y = graph[x]

    if not visited[y] :
        is_cycle(y)
    elif not finished[y] :
        while y != x :
            result.append(y)
            y = graph[y]
        result.append(x)

    finished[x] = True


n = int(input()) 
graph = [0] * (n + 1)

for i in range(1, n + 1) :
    graph[i] = int(input())

visited = [False] * (n + 1)
finished = [False] * (n + 1)
result = []

for x in range(1, n + 1) :
    if not visited[x] :
        is_cycle(x)

print(len(result))

result = sorted(result)
for x in result :
    print(x)