import sys
input = sys.stdin.readline

sys.setrecursionlimit(int(1e6))

def is_cycle(x):
    visited[x] = True 
    y = graph[x] 

    if not visited[y]:
        is_cycle(y)
    
    elif not finished[y]: 
        
        while y != x:
            result.append(y)
            y = graph[y]
        result.append(x)

    finished[x] = True

# 각 테스트 케이스 수행
for _ in range(int(input())): 
    n = int(input())
    graph = [0] + list(map(int, input().split()))

    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    result = []

    # 각 노드에서 DFS로 사이클 판별
    for x in range(1, n + 1):
        if not visited[x]:
            is_cycle(x)
            
    print(n - len(result))