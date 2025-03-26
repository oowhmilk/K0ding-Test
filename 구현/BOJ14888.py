from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split(' ')))
opr_num = list(map(int, input().split(' ')))

opr = []
for i in range(len(opr_num)) :
    if i == 0 :
        for _ in range(opr_num[i]) :
            opr.append('+')
    elif i == 1 :
        for _ in range(opr_num[i]) :
            opr.append('-')
    elif i == 2 :
        for _ in range(opr_num[i]) :
            opr.append('*')
    elif i == 3 :
        for _ in range(opr_num[i]) :
            opr.append('/')

comb = list(permutations(opr))

result = []
for x in comb :
    check = num[0]
    for i in range(len(x)) :
        if x[i] == '+' :
            check = check + num[i + 1]
        elif x[i] == '-' :
            check = check - num[i + 1]
        elif x[i] == '*' :
            check = check * num[i + 1]
        elif x[i] == '/' :
            if check > 0 :
                check = check // num[i + 1]
            else :
                check = -check
                check = -(check // num[i + 1])
    
    result.append(check)

print(max(result))
print(min(result))