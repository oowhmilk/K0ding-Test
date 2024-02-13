import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 1
for i in range(0, n) :
    right = arr[i]

    count = 0
    before = 0
    for j in range(i, 0, -1) :
        left = arr[j]

        if before < left and left < right:
            before = left
            count += 1
            print(i, j)

    ans = max(ans, count + 1)

print(ans)