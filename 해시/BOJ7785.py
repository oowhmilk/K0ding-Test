import sys
input = sys.stdin.readline

n = int(input())

dic = {}
for _ in range(n) :
    name, which = input().strip().split(' ')

    if name in dic :
        dic.pop(name)
    else :
        dic[name] = 1

dic = sorted(dic, reverse = True)
for x in dic :
    print(x)