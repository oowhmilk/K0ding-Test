import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n) :
    arr.append(int(input()))

check = set(arr)
result = 0

for i in range(n) :
    for j in range(i, n) :
        for k in range(j, n) :
            if arr[i] + arr[j] + arr[k] in check :
                result = max(result, arr[i] + arr[j] + arr[k])

print(result)