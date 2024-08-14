import sys
input = sys.stdin.readline

dict = {}

for _ in range(int(input())) : 
    name, behavior = input().strip().split(' ')

    if name in dict :
        dict.pop(name)
    else :
        dict[name] = 1

dict = sorted(dict, reverse = True)

for x in dict :
    print(x)