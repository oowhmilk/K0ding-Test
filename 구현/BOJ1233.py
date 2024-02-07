import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

s1 = arr[0]
s2 = arr[1]
s3 = arr[2]

dic = dict()

for i in range(1, s1 + 1) :
    for j in range(1, s2 + 1) :
        for k in range(1, s3 + 1) :
            value = i + j + k
            if value not in dic :
                dic[value] = 1
            else :
                dic[value] += 1

count = -1
answer = int(1e9)
for (key, value) in dic.items() :
    if count < value :
        count = value
        answer = key
    elif count == value :
        answer = min(answer, key)
    
print(answer)