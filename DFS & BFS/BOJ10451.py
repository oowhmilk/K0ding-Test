# import sys
# input = sys.stdin.readline

# def get_parent(parent, x) :
#     if parent[x] == x :
#         return x 
#     return get_parent(parent, parent[x])

# def union_parent(parent, x, y) :
#     a = get_parent(parent, x)
#     b = get_parent(parent, y)

#     if a < b :
#         parent[b] = a
#     else :
#         parent[a] = b

# def find_parent(parent, x, y) :
#     a = get_parent(parent, x)
#     b = get_parent(parent, y)

#     if a == b :
#         return True
#     else :
#         return False

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

for _ in range(int(input())) :
    n = int(input())
    arr = []

    str = list(map(int, input().split(' ')))
    for i in range(n) :
        arr.append((i + 1, str[i]))

    cycle = set()
    parent = {}

    for i in range(1, n + 1) :
        parent[i] = i

    for a, b in arr :
        if not find_parent(parent, a, b) :
            union_parent(parent, a, b)

    for i in range(1, n + 1) :
        cycle.add(get_parent(parent, i))

    print(len(cycle))

# for _ in range(int(input())) :
#     n = int(input())
#     arr = []

#     str = list(map(int, input().split(' ')))
#     for i in range(len(str)) :
#         arr.append((i + 1, str[i]))

#     cycle = set()
#     parent = {}
#     for i in range(1, n + 1) :
#         parent[i] = i
     
#     for a, b in arr :
#         if not find_parent(parent, a, b) :
#             union_parent(parent, a, b)

#     for i in range(1, n + 1) :
#         cycle.add(get_parent(parent, i))

#     print(len(cycle))


import sys
input = sys.stdin.readline

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

    arr = []
    str = list(map(int, input().split(' ')))
    for x in str :
        arr.append(x - 1)

    count = 0
    visited = [False] * n
    finished = [False] * n
    result = []
    for i in range(n) :
        if not visited[i] :
            is_cycle(i)
            count += 1

    print(count)