import sys
input = sys.stdin.readline

ans = []

for _ in range(int(input())) :
    n = int(input())
    arr = list(map(int, input().split(' ')))
    arr = sorted(arr)

    result = [0] * (len(arr))
    left = 0
    right = len(arr) - 1

    for i in range(n) :
        if right < left :
            break

        if i % 2 == 0 :
            result[left] = arr[i]
            left += 1
        else : 
            result[right] = arr[i]
            right -= 1

    dif = 0
    for i in range(len(result) - 1) :
        dif = max(dif, abs(result[i] - result[i + 1]))

    ans.append(dif)

for data in ans :
    print(data)