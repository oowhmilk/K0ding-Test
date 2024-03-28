import sys
input = sys.stdin.readline

s = input()

arr = []

check = s[0]
arr.append(check)
for i in range(1, len(s)):
    if check == s[i] :
        continue
    else :
        check = s[i]
        arr.append(check)

one = 0
zero = 0
for i in range(len(arr)) :
    if arr[i] == '1' :
        one += 1
    elif arr[i] == '0' :
        zero += 1

print(min(one, zero))


data = input()

count0 = 0 # 전부 0 으로 바꾸는 경우
count1 = 0 # 전부 1 로 바꾸는 경우


if data[0] == '1' :
    count0 += 1
else :
    count1 += 1

for i in range(len(data) - 1) :
    if data[i] != data[i + 1] :
        if data[i + 1] == '1' :
            count0 += 1
        else :
            count1 += 1

print(min(count0, count1))