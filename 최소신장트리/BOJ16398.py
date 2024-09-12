import sys
input = sys.stdin.readline

def get_parent(parent, x) :
    if parent[x] == x :
        return x
    return get_parent(parent, parent[x])

def union_parent(parent, x, y) :
    a = get_parent(parent, x)
    b = get_parent(parent, y)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

def find_parent(parent, x, y) : 
    a = get_parent(parent, x)
    b = get_parent(parent, y)

    if a == b :
        return True
    else :
        return False

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]  # 각 행성간의 플로우 관리 비용
parent = [i for i in range(n)]  # 부모 노드 정보

edges = []  
for i in range(1, n):
    for j in range(i):
        edges.append((i, j, arr[i][j]))
edges.sort(key = lambda x : x[2])  

result = 0
for a, b, c in edges :
    if not find_parent(parent, a, b) :
        union_parent(parent, a, b)
        result += c

print(result)