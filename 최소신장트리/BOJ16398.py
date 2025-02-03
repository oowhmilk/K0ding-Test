import sys
input = sys.stdin.readline

def find_parent(parent, a, b) :
    x = get_parent(parent, a)
    y = get_parent(parent, b)

    if x == y :
        return True
    else :
        return False
    
def get_parent(parent, x) :
    if parent[x] == x :
        return x 
    return get_parent(parent, parent[x])

def union_parent(parent, a, b) :
    x = get_parent(parent, a)
    y = get_parent(parent, b)

    if x < y :
        parent[y] = x
    else :
        parent[x] = y 

n, m = map(int, input().split(' '))

arr = []
for _ in range(m) :
    a, b, c = map(int, input().split(' '))
    arr.append((a, b, c))

parent = [i for i in range(n + 1)]
arr.sort(key = lambda x : x[2])

result = 0
max_value = 0
for a, b, c in arr :
    if not find_parent(parent, a, b) :
        union_parent(parent, a, b)
        result += c 
        max_value = max(max_value, c)

print(result - max_value)