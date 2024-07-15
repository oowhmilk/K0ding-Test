## 최소 신장트리 문제
## 크루 스칼 알고리즘 
## 간선 들 중 최소 비용인 간선들만 확인해서 가져온다 (단, 그래프가 사이클이 발생하지 않도록 간선을 선택)
## Union - Find 알고리즘 이용해서 두 개의 정점을 합칠때 Union 이용하고  두 개의 정점이 동일한 패널티를 가지고 있을때는 Find 이용
## 합치기 전에 Find 를 이용해서 두 개의 정점이 같은 부모를 가진다면 합치지 못하도록 하는 방식

# import math
# import sys
# input = sys.stdin.readline

# def get_distance(p1, p2) :
#     a = p1[0] - p2[0]
#     b = p1[1] - p2[1]
#     return math.sqrt((a * a) + (b * b))

# def get_parent(parent, n) :
#     if parent[n] == n :
#         return n 
#     return get_parent(parent, parent[n])

# def union_parent(parent, a, b) :
#     a = get_parent(parent, a)
#     b = get_parent(parent, b)
#     if a < b :
#         parent[b] = a
#     else :
#         parent[a] = b

# def find_parent(parent, a, b) :
#     a = get_parent(parent, a)
#     b = get_parent(parent, b)
#     if a == b :
#         return True
#     else : 
#         return False 


# edges = [] # 점들 사이의 거리
# parent = {}
# locations = [] # 점 위치

# n, m = map(int, input().split(' '))

# for i in range(n) :
#     x, y = map(int, input().split(' '))
#     locations.append((x, y))

# length = len(locations)

# for i in range(length - 1) :
#     for j in range(i + 1, length) :
#         edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

# for i in range(1, n + 1) :
#     parent[i] = i

# for i in range(m) :
#     a, b = map(int, input().split(' '))
#     union_parent(parent, a, b)


# edges.sort(key = lambda x : x[2]) # 크루스칼 알고리즘은 거리 순으로 정렬해서 거리가 짧은 것 부터 고른다 

# result = 0
# for a, b, cost in edges :
#     if not find_parent(parent, a, b) :
#         union_parent(parent, a, b)
#         result += cost

# print("%0.2f" % result)


import math
import sys
input = sys.stdin.readline

def get_distance(p1, p2) :
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return math.sqrt((x * x) + (y * y))

def get_parent(parent, n) :
    if parent[n] == n :
        return n
    return get_parent(parent, parent[n])

def union_parent(parent, a, b) :
    a = get_parent(parent, a)
    b = get_parent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

def find_parent(parent, a, b) :
    a = get_parent(parent, a)
    b = get_parent(parent, b)

    if a == b :
        return True
    else : 
        return False

edges = []
parent = {}
locations = []

n, m = map(int, input().split(' '))
for i in range(n) :
    x, y = map(int, input().split(' '))
    locations.append((x, y))

length = len(locations)

for i in range(length - 1) :
    for j in range(i + 1, length) :
        edges.append((i + 1, j + 1, get_distance(locations[i], locations[j])))

for i in range(1, n + 1) :
    parent[i] = i

for i in range(m) :
    a, b = map(int, input().split(' '))
    union_parent(parent, a, b)

edges.sort(key = lambda x : x[2])

result = 0
for a, b, cost in edges :
    if not find_parent(parent, a, b) :
        union_parent(parent, a, b)
        result += cost

print("0.2f" % result)