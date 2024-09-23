import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

sum = [0]
tmp = 0
for x in arr :
    tmp = tmp + x
    sum.append(tmp)

for _ in range(m) :
    x, y = map(int, input().split(' '))
    print(sum[y] - sum[x - 1])