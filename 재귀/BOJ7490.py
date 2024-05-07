# import sys
# input = sys.stdin.readline

# from itertools import product

# t = int(input())

# arr = [' ', '+', '-']
# string = []

# for _ in range(t) :
#     n = int(input())

#     num = []
#     cal = []
#     result = 1

#     for i in range(n) :
#         num.append(i+1)

#     cal = list(product(arr, repeat = n-1))

#     for i in range(len(cal)) :

#         recent = 1
#         for j in range(len(cal[i])) :
            
#             if cal[i][j] == '+' :
#                 result += num[j + 1]
#                 recent = num[j + 1]

#             elif cal[i][j] == '-' :
#                 result -= num[j + 1]
#                 recent = -num[j + 1]

#             elif cal[i][j] == ' ' :
#                 result -= recent

#                 if recent < 0 :
#                     recent = ( recent * 10 ) - num[j + 1]
#                 else :
#                     recent = ( recent * 10 ) + num[j + 1]

#                 result += recent 

#         if result == 0 :
#             for j in range(len(cal[i])) :
#                 string.append(num[j])
#                 string.append(cal[i][j])
#             string.append(num[len(num) - 1])
#             string.append('\n')
#         else :
#             result = 1

#     string.append('\n')

# for x in string :
#     print(x, end = '')


import copy

def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array, n)
    array.pop()
    array.append('+')
    recursive(array, n)
    array.pop()
    array.append('-')
    recursive(array, n)
    array.pop()

test_case = int(input())
for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([], n - 1)
    integers = [i for i in range(1, n + 1)]
    for operators in operators_list:
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()