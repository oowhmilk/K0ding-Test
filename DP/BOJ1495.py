import sys
input = sys.stdin.readline

n, s, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

volume = [-1] * (m + 1)
volume[s] = 0

for i in range(len(arr)) :
    last = -1
    check = []
    for j in range(len(volume)) :

        if volume[j] == i :
            check.append(j)

    for k in range(len(check)) :
        if 0 <= check[k] - arr[i]  :
            volume[check[k] - arr[i]] = i + 1
        if check[k] + arr[i] <= m :
            volume[check[k] + arr[i]] = i + 1

# print(volume)

result = []
for i in range(len(volume)) :
    if volume[i] == n :
        result.append(i)

if len(result) == 0:
    print(-1)
else : 
    print(max(result))
