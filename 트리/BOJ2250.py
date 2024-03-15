import sys
input = sys.stdin.readline

class Node :
    def __init__(self, data, left_node, right_node, level) :
        self.parent = -1
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        self.level = level

def in_order(node, depth) :
    depth += 1
    node.level = depth
    if node.left_node != -1 :
        in_order(tree[node.left_node], depth)

    arr.append((node.level, node.data))

    if node.right_node != -1 :
        in_order(tree[node.right_node], depth)

n = int(input())

tree = {}
for i in range(n) :
    data, left_node, right_node = map(int, input().split(' '))
    tree[data] = Node(data, left_node, right_node, 0)
    if left_node != -1 :
        tree[left_node].parent = data
    if right_node != -1 :
        tree[right_node].parent = data

root = -1
for i in range(1, n + 1):
    if tree[i].parent == -1 :
        root = i

arr = []
in_order(tree[root], 0)

max_depth = max(arr, key = lambda x: x[0])[0]

result = {}
for i in range(2, max_depth + 1) :

    first = 2**31
    last = 0
    
    for j in range(len(arr)) :
        if arr[j][0] == i :
            if first > j :
                first = j
                last = j
            elif last < j :
                last = j

    result[i] = last - first

target = max(result.values())

ans = []
for level, width in result.items() :
    if width == target :
        ans.append((level, width))

print(sorted(ans)[0][0], sorted(ans)[0][1] + 1)
