import sys
input = sys.stdin.readline

n = int(input())
have = list(map(int, input().split(' ')))
have = set(have)

m = int(input())
check = list(map(int, input().split(' ')))

for x in check :
    if x in have :
        print(1, end = ' ')
    else :
        print(0, end = ' ')