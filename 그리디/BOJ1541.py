import sys
input = sys.stdin.readline

arr = list(map(str, input().strip().split('-')))

answer = 0
for i in arr[0].split('+') :
    answer += int(i)

for i in arr[1:] :
    for j in i.split('+') :
        answer -= int(j)

print(answer)