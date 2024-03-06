import sys
input = sys.stdin.readline

n = input()
arr = list(n)

sort = []
for i in range(len(arr) - 1) :
    sort.append(int(arr[i]))

sort = sorted(sort)

for i in range(len(sort)) :
    print(sort[len(sort) - i - 1], end = '')


arr = input() 
for i in range(9, -1, -1) :
    for j in arr :
        if int(j) == i :
            print(i, end = '')