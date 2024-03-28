import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n) :
    arr.append(int(input()))

arr.sort()

dif = 0
for i in range(n) :
    dif += abs(arr[i] - (i + 1))

print(dif)