import sys
input = sys.stdin.readline

n = int(input())

data =[]

for _ in range(n) :
    num = int(input())

    if num == 0 :
        data.pop(-1)
    else :
        data.append(num)

result = 0

for i in range(len(data)) :
    result += data[i]

print(result)