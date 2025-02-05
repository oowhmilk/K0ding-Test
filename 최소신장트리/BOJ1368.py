import sys
input = sys.stdin.readline

def find_parent(parent, a, b) :
    x = get_parent(parent, a)
    y = get_parent(parent, b)

    if x == y :
        return True
    else :
        return False
    
def union_parent(parent, a, b) :
    x = get_parent(parent, a)
    y = get_parent(parent, b)

    if x < y :
        parent[y] = x
    else :
        parent[x] = y

def get_parent(parent, x) :
    if parent[x] == x :
        return x
    return get_parent(parent, parent[x])

n = int(input())

arr = [0]
for _ in range(n) :
    arr.append(int(input()))

non = []
non.append(arr)
for i in range(1, n + 1) :
    non.append([arr[i]] + list(map(int, input().split(' '))))

water = []
for i in range(n + 1) :
    for j in range(n + 1) :
        water.append((i, j, non[i][j]))

water.sort(key = lambda x : x[2])

parent = [i for i in range(n + 1)]

total = 0
for a, b, c in water :
    if not find_parent(parent, a, b) :
        union_parent(parent, a, b)
        total += c

print(total)