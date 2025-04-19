# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)

# def find_parent(x, y) :
#     a = get_parent(x)
#     b = get_parent(y)

#     if a == b :
#         return True
#     else :
#         return False

# def union_parent(x, y) :
#     a = get_parent(x)
#     b = get_parent(y)

#     if a < b :
#         parent[b] = a
#     else :
#         parent[a] = b

# def get_parent(x) :
#     if parent[x] != x :
#         parent[x] = get_parent(parent[x])
#         return parent[x]
#     return x

# v, e = map(int, input().split(' '))

# arr = []
# for _ in range(e) :
#     a, b, c = map(int, input().split(' '))
#     arr.append((a, b, c))

# arr = sorted(arr, key = lambda x : x[2])

# parent = [i for i in range(v + 1)]
# answer = 0

# for a, b, c in arr :
#     if not find_parent(a, b) :
#         union_parent(a, b)
#         answer += c

# print(answer)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def find_parent(a, b) :
    x = get_parent(parent, a)
    y = get_parent(parent, b)

    if x == y :
        return True
    else :
        return False
    
def union_parent(a, b) :
    x = get_parent(parent, a)
    y = get_parent(parent, b)

    if x < y :
        parent[y] = x
    else :
        parent[x] = y

def get_parent(parent, x) :
    if parent[x] != x :
        return get_parent(parent, parent[x])
    return x

v, e = map(int, input().split(' '))
arr = []
for _ in range(e) :
    a, b, c = map(int, input().split(' '))
    arr.append((a, b, c))

arr = sorted(arr, key = lambda x : x[2])

parent = [i for i in range(v + 1)]
cost = 0
for a, b, c in arr :
    if not find_parent(a, b) :
        union_parent(a, b)
        cost += c

print(cost)