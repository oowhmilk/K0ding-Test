import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

arr = list(map(int, input().split(' ')))
arr.sort()

if k >= n :
    print(0)
    sys.exit()

dif = []
for i in range(len(arr) - 1) :
    dif.append(arr[i + 1] - arr[i])

dif.sort(reverse = True)

for i in range(k - 1) :
    dif[i] = 0

print(sum(dif))