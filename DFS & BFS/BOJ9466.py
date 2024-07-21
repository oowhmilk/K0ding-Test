# 현재 노드 방문 처리
# 다음 노드를 아직 방문하지 않았다면 사이클 판단
# 다음 노드를 방문한 적이 있고 완료되지 않았다면 => 사이클 발생
# 사이클에 포함된 노드 저장
# 현재 노드의 처리 완료
# 방문 여부 visited
# 완료 여부 finished 
# 두 개의 list 로 판단

# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(int(1e6))

# def is_cycle(x):
#     visited[x] = True 
#     y = graph[x] 

#     if not visited[y]:
#         is_cycle(y)
    
#     elif not finished[y]: 
        
#         while y != x:
#             result.append(y)
#             y = graph[y]
#         result.append(x)

#     finished[x] = True

# # 각 테스트 케이스 수행
# for _ in range(int(input())): 
#     n = int(input())
#     graph = [0] + list(map(int, input().split()))

#     visited = [False] * (n + 1)
#     finished = [False] * (n + 1)
#     result = []

#     # 각 노드에서 DFS로 사이클 판별
#     for x in range(1, n + 1):
#         if not visited[x]:
#             is_cycle(x)
            
#     print(n - len(result))


import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

def is_cycle(x) :
    visited[x] = True
    y = arr[x]

    if not visited[y] :
        is_cycle(y)
    elif not finished[y] :
        while y != x :
            result.append(y)
            y = arr[y]
        result.append(x)

    finished[x] = True

for _ in range(int(input())) :
    n = int(input())
    arr = [0] * (n + 1)
    enter = list(map(int, input().split(' ')))

    for i in range(len(enter)) :
        arr[i + 1] = enter[i]

    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    result = []

    for x in range(1, n + 1) :
        if not visited[x] :
            is_cycle(x)

    print(n - len(result))