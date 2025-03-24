import sys
input = sys.stdin.readline

n = int(input())
check = list(map(int, input().split(' ')))

arr = [0] * n

for i in range(len(check)) :

    count = 0
    for j in range(len(arr)) :

        if count == check[i] :
            for k in range(j, len(arr)) :
                if arr[k] == 0 :
                    arr[k] = i + 1
                    break
            break

        if arr[j] == 0 :
            count += 1


for x in arr :
    print(x, end = ' ')