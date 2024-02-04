import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
arr = list(map(int, input().split()))
arr = sorted(arr)

from itertools import product
result = list(product(arr, repeat = m))

result = sorted(result)

for i in range(len(result)) :
    for j in range(m) : 
        print(result[i][j], end = ' ')
    print('')