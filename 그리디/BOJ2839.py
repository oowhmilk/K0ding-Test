import sys
input = sys.stdin.readline

n = int(input())
answer = 0

while 0 <= n :
    if n % 5 == 0 :
        answer += (n // 5)
        print(answer)
        sys.exit()

    n -= 3
    answer += 1

print(-1)
