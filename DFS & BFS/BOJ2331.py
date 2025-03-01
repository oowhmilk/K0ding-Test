import sys
input = sys.stdin.readline

a, p = map(int, input().split(' '))
arr = [a]

while True :
    value = arr[-1]

    tmp = 0
    for s in str(value) :
        tmp += int(s) ** p

    if tmp in arr :
        break

    arr.append(tmp)

for i in range(len(arr)) :
    if arr[i] == tmp :
        print(i)