import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))

dic = {}
for x in arr :
    if x not in dic :
        dic[x] = 1
    else :
        dic[x] += 1

m = int(input())
arr = list(map(int, input().split(' ')))

for x in arr :
    if x not in dic :
        print(0, end = ' ')
    else :
        print(dic[x], end = ' ')