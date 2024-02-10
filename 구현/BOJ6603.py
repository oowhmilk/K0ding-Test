import sys
input = sys.stdin.readline

from itertools import combinations


while True:
    arr = list(map(int,input().split()))

    if arr[0] == 0:
        break

    else :
        value = arr[1 : ]
        for result in combinations(value, 6):
            temp = list(map(str, result))
            print(" ".join(temp))

    print()
