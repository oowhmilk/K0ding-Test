# import sys
# input = sys.stdin.readline

# n = int(input())
# first = list(map(int, input().split(' ')))
# second = list(map(int, input().split(' ')))

# first = sorted(first)
# second = sorted(second)

# result = 0
# for i in range(n) :
#     result += (first[i] * second[n - 1 - i])

# print(result)


import sys
input = sys.stdin.readline

n = int(input())
fir = list(map(int, input().split(' ')))
sec = list(map(int, input().split(' ')))

fir.sort()
sec.sort(reverse=True)

result = 0
for i in range(n) :
    result += fir[i] * sec[i]

print(result)