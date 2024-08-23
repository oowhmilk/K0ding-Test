# 우물을 팔 때 드는 비용을 0번 논에 논을 연결하는 비용이라고 생각하고 문제를 접근
# 이때 모든 논을 연결하는데 최소 비용을 확인할 수 있다.
# 따라서 최소신장트리 MST 를 사용하는 방식이다.

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
arr = [] 

for i in range(1, n + 1):
    arr.append([0, i, int(input())])
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if i != j:
            arr.append([i + 1, j + 1, tmp[j]])

arr.sort(key=lambda x: x[2])

parent = {}
for i in range(n + 1) :
    parent[i] = i

answer = 0
for a, b, c in arr :
    if not find_parent(parent, a, b) :
        union_parent(parent, a, b)
        answer += c

print(answer)