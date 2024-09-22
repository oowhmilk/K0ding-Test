import sys
input = sys.stdin.readline

for _ in range(int(input())) :

    dict = {}
    for _ in range(int(input())) :
        value, key = input().strip().split(' ')

        if key in dict :
            dict[key] += 1
        else :
            dict[key] = 1

    count = 1
    for x in dict.values() :
        count *= (x + 1)

    print(count - 1)