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

n, m = map(int, input().split(' '))

arr = []
for _ in range(m + 1) :
    a, b, c = map(int, input().split(' '))
    arr.append((a, b, c))

arr.sort(key = lambda x : x[2])

parent = [i for i in range(n + 1)]
count_low = 0
for a, b, c in arr :
    if not find_parent(parent, a, b) :
        union_parent(parent, a, b)
        count_low += c

arr.sort(key = lambda x : -x[2])

parent = [i for i in range(n + 1)]
count_high = 0
for a, b, c in arr :
    if not find_parent(parent, a, b) :
        union_parent(parent, a, b)
        count_high += c

print(abs(count_high ** 2 - count_low ** 2))