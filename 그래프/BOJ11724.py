import sys
input = sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y) :
    a = find_parent(parent, x)
    b = find_parent(parent, y)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1) :
    parent[i] = i

for i in range(m) :
    x, y = map(int, input().split())
    union_parent(parent, x , y)

counter = set()
for i in range(1, n + 1):
    counter.add(find_parent(parent, i))

print(len(counter))