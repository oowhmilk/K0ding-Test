import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
arr = []

for _ in range(n) :
    arr.append(int(input()))

arr.sort(reverse = True)

coin = 0
for i in range(len(arr)) :
    
    if k // arr[i] != 0 :
        coin = coin + (k // arr[i])
        k = k % arr[i]

print(coin)