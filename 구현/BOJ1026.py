import sys
input = sys.stdin.readline

n = int(input())
first = list(map(int, input().split(' ')))
second = list(map(int, input().split(' ')))

first = sorted(first)
second = sorted(second)

result = 0
for i in range(n) :
    result += (first[i] * second[n - 1 - i])

print(result)