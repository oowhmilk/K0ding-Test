import sys
input = sys.stdin.readline

from collections import deque

def bfs(v) :
    q = deque([v])
    visited[v] = 0

    while q :
        x = q.popleft()
        color = visited[x]

        for y in graph[x] :
            if visited[y] == -1 :
                visited[y] = (color + 1) % 2
                q.append(y)
            elif visited[y] == 0 :
                if color == 0 :
                    return False
            else :
                if color == 1 :
                    return False
                
    return True




k = int(input())

for _ in range(k) :
    V, E = map(int, input().split(' '))

    graph = [[] for _ in range(V + 1)]
    

    for _ in range(E) :
        u, v = map(int, input().split(' '))
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [-1] * (V + 1)

    cnt = 0
    for i in range(1, V + 1) :
        if visited[i] == -1 :
            check = bfs(i)
            if check == False :
                cnt = 1

    if cnt == 1 :
        print("NO")
    else :
        print("YES")