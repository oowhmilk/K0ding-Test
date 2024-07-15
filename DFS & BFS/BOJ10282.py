# import sys
# input = sys.stdin.readline

# def visit(v) :
#     visited[v] = True
#     global time, count

#     for e, s in arr[v]:
#         if not visited[e] :
#             time += s
#             count += 1
#             visit(e)

# for _ in range(int(input())) :
#     n, d, c = map(int, input().split(' ')) # n : 컴퓨터 개수, d : 의존성 개수, c : 해킹당한 컴퓨터의 번호
#     arr = [[] for _ in range(n + 1)]  # 컴퓨터 번호를 1부터 시작하므로 크기를 n + 1로 설정
#     visited = [False] * (n + 1)

#     for _ in range(d) :
#         a, b, s = map(int, input().split(' '))
#         arr[b].append((a, s))

#     time = 0
#     count = 1
#     visit(c)
#     print(count, time)  # 해킹된 컴퓨터의 개수 출력, 방문한 컴퓨터 수에서 해킹당한 컴퓨터를 제외


import sys
from collections import deque

input = sys.stdin.readline

def bfs(v) :
    global time, count
    q = deque([v])
    visited[v] = True

    while q :
        v = q.popleft()

        for e, s in arr[v] :
            if not visited[e] :
                q.append(e)
                visited[e] = True
                count += 1
                time += s



for _ in range(int(input())) :
    n, d, c = map(int, input().split(' '))
    arr = [[] for _ in range(n + 1)]

    for _ in range(d) :
        a, b, s = map(int, input().split(' '))
        arr[b].append((a, s))

    visited = [False] * (n + 1)
    time = 0
    count = 1

    bfs(c)

    print(count, time)