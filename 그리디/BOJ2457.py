import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n) :
    start_m, start_d, end_m, end_d = map(int, input().split(' '))
    arr.append([start_m * 100 + start_d, end_m * 100 +end_d])

arr.sort(key = lambda x : (x[0], x[1]))

cnt = 0
end = 0
start = 301

while arr :
    if 1130 < start or start < arr[0][0] :
        break

    for _ in range(len(arr)) :
        if arr[0][0] <= start :
            if end <= arr[0][1] :
                end = arr[0][1]

            arr.remove(arr[0])
        else :
            break
    
    start = end
    cnt += 1

if start <= 1130 :
    print(0)
else :
    print(cnt)