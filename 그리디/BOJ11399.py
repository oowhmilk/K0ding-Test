import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

check = [0] * (n + 1)
for i in range(1, n + 1) :
    check[i] = check[i - 1] + arr[i - 1]

print(sum(check))