# 경우의 수는 단 2가지만 고려하면 된다.
# 모든 수를 0 으로 만드는 경우, 모든 수를 1 로 만드는 경우 
# 모든 수를 1로 만드는 경우 : 첫번째 원소가 0 인 경우 , 2개씩 원소를 비교할 때, 1 에서 0 으로 바뀌는 경우 => 각 경우 마다 +1 씩 증가
# 모든 수를 0 으로 만드는 경우 : 첫번째 원소가 1 인 경우, 2개씩 원소를 비교할 때, 0 에서 1 로 바뀌는 경우 => 각 경우 마다 +1 씩 증가 

import sys
input = sys.stdin.readline

data = input()

count0 = 0 # 모든 수를 0 으로 만드는 경우
count1 = 0 # 모든 수를 1 로 만드는 경우 

if data[0] == 0 :
    count1 += 1
else :
    count0 += 1

for i in range(len(data) - 1) :
    if data[i] != data[i + 1] :
        if data[i + 1] == 1 :
            count0 += 1
        else :
            count1 += 1

print(min(count0, count1))

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