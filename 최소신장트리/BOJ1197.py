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

v, e = map(int, input().split(' '))

arr = []
for _ in range(e) :
    a, b, c = map(int, input().split(' '))
    arr.append((a, b, c))

arr.sort(key = lambda x : x[2])

parent = {}
for i in range(1, v + 1) :
    parent[i] = i

answer = 0
for a, b, c in arr :
    if not find_parent(parent, a, b) :
        union_parent(parent, a, b)
        answer += c

print(answer)
