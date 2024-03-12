import sys
input = sys.stdin.readline

from itertools import product

t = int(input())

arr = [' ', '+', '-']
string = []

for _ in range(t) :
    n = int(input())

    num = []
    cal = []
    result = 1

    for i in range(n) :
        num.append(i+1)

    cal = list(product(arr, repeat = n-1))

    for i in range(len(cal)) :

        recent = 1
        for j in range(len(cal[i])) :
            
            if cal[i][j] == '+' :
                result += num[j + 1]
                recent = num[j + 1]

            elif cal[i][j] == '-' :
                result -= num[j + 1]
                recent = -num[j + 1]

            elif cal[i][j] == ' ' :
                result -= recent

                if recent < 0 :
                    recent = ( recent * 10 ) - num[j + 1]
                else :
                    recent = ( recent * 10 ) + num[j + 1]

                result += recent 

        if result == 0 :
            for j in range(len(cal[i])) :
                string.append(num[j])
                string.append(cal[i][j])
            string.append(num[len(num) - 1])
            string.append('\n')
        else :
            result = 1

    string.append('\n')

for x in string :
    print(x, end = '')