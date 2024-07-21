# 트리 : 사이클이 없는 연결 요소
# DFS 를 이용해 트리의 개수를 계산 
# 무방향 그래프 내에서 
# 특정 노드에서 DFS 를 수행하는 과정에서 인접 노드가 이미 방문한 보드라면 사이클

# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(100000)

# def is_cycle(x, prev) :

#     visited[x] = True # 현재 노드 방문 처리
    
#     for y in graph[x] : # 다음 노드를 하나씩 확인
        
#         if visited[y] :
#             if y != prev : # 다음 노드가 방문한 노드이고 이전 노드가 아니라면 사이클
#                 return True
#         else : 
#             if is_cycle(y, x) : # 다음 노드가 방문한 노드가 아닌데 다음 노드로 인해 사이클이 발생한다면 사이클
#                 return True
            
#     return False


# case = 0
# while 1 :
#     n, m = map(int, input().split(' '))

#     if n == 0 and m == 0 : 
#         break

#     case += 1

#     graph = [[] for _ in range(n + 1)]

#     for _ in range(m) :
#         x, y = map(int, input().split(' '))

#         graph[x].append(y)
#         graph[y].append(x)

#     visited = [False] * (n + 1)

#     cnt = 0
#     for i in range(1, n + 1) : 
#         if not visited[i] : 
#             if not is_cycle(i, 0) :
#                 cnt += 1

#     if cnt == 0 :
#         print(f'Case {case}: No trees.')
#     elif cnt == 1 :
#         print(f'Case {case}: There is one tree.')
#     else : 
#         print(f'Case {case}: A forest of {cnt} trees.')


import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

def is_cycle(x, prev) :
    visited[x] = True
    
    for y in arr[x] :
        if visited[y] :
            if y != prev :
                return True
        else :
            if is_cycle(y, x) :
                return True
    
    return False

case = 0
while True :
    n, m = map(int, input().split(' '))
    case += 1

    if n == 0 and m == 0 :
        break

    arr = [[0] for _ in range(n + 1)]
    for _ in range(m) :
        x, y = map(int, input().split(' '))
        arr[x].append(y)
        arr[y].append(x)

    visited = [False] * (n + 1)
    cnt = 0

    for i in range(1, n + 1) :
        if not visited[i] :
            if not is_cycle(i, 0) :
                cnt += 1

    if cnt == 0 :
        print(f'Case {case}: No trees.')
    elif cnt == 1 :
        print(f'Case {case}: There is one tree.')
    else : 
        print(f'Case {case}: A forest of {cnt} trees.')
