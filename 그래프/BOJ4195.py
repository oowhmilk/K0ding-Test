case = int(input())

result = []

for _ in range(case) :
    relation = int(input())

    friends = set()
    for i in range(relation) :
        new_set = set(map(str, input().split(' ')))
        friends.update(new_set)

        size = len(friends)

        if size == (i+1) * 2 :
            result.append(2)
        else :
            result.append(size)
        
for i in range(len(result)) :
    print(result[i])



## 풀이
# Union - Find algo
def find(x) :
    if x == parent[x]:
        return x
    else :
        p = find(parent[x])
        parent[x] = p
        return parent[x]
    
def union(x, y) :
    x = find(X)
    y = find(y)
    parent[y] = x

parent= []

for i in range(0, 5) :
    parent.append(i)

union(1, 4)
union(2, 4)

for i in range(1, len(parent)) :
    print(find(i), end=' ')
        