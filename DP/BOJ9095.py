import sys
input = sys.stdin.readline

for _ in range(int(input())) :
    n = int(input())
    arr = [1, 2, 4]

    if 3 < n :
        for i in range(3, n) :
            value = 0
            for j in range(1, 4) :
                value += arr[i - j]
            arr.append(value)

    print(arr[n - 1])