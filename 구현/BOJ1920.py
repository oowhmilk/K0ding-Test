n = int(input())
a = set(map(int, input().split(' ')))
m = int(input())
b = list(map(int, input().split(' ')))

for value in b :
    if value not in a:
        print('0')
    else :
        print('1')
