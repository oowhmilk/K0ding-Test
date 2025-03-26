import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
b, c = map(int, input().split(' '))

count = 0
for x in arr :
    x -= b
    count += 1

    if x < 0 :
        continue
    else :
        if x % c == 0 :
            count += int(x // c)
        else :
            count += int(x // c) + 1

print(count)