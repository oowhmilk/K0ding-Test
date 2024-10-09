import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
a = set(map(int, input().split(' ')))
b = set(map(int, input().split(' ')))

arr = []
for x in a : 
    if x not in b :
        arr.append(x)

if len(arr) == 0 :
    print(len(arr))
    sys.exit()
else : 
    print(len(arr))
    arr.sort()
    for x in arr :
        print(x, end = ' ')