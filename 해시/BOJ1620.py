import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

dict1 = {}
dict2 = {}
for i in range(n) :
    name = input().strip()

    dict1[name] = i + 1
    dict2[i + 1] = name

for _ in range(m) :
    question = input().strip()

    if question.isdigit() :
        print(dict2[int(question)])
    else :
        print(dict1[question])