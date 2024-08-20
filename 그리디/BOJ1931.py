import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n) :
    x, y = map(int, input().split(' '))
    arr.append((x, y))

arr.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = arr[0][1]
for i in range(1, n) :
    if end_time <= arr[i][0] :
        end_time = arr[i][1]
        cnt += 1

print(cnt)