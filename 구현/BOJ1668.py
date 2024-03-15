import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n) :
    arr.append(int(input()))

left = 0
max = 0
for i in range(len(arr)) :
    if max < arr[i] :
        max = arr[i]
        left += 1
    
arr.reverse()
right = 0
max = 0
for i in range(len(arr)) :
    if max < arr[i] :
        max = arr[i]
        right += 1

print(left)
print(right)
