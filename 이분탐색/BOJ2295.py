import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n) : 
    arr.append(int(input()))

result = set(arr)
max_sum = -1

for i in range(n):
    for j in range(i, n):  
        for k in range(j, n):
            s = arr[i] + arr[j] + arr[k]
            if s in result:
                max_sum = max(max_sum, s)

print(max_sum)