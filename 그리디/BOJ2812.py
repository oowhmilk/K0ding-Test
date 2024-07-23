# 현재 원소가 스택의 top() 보다 크다면, 작을 때까지 스택에서 pop()
# 현재 원소를 스택에 삽입

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# data = input().strip()

# delete = 0
# stack = []

# for x in data :
#     while len(stack) > 0 and stack[-1] < x :
#         if delete == k :
#             break
#         else :
#             stack.pop()
#             delete += 1

#     stack.append(x)

# for i in range(k - delete) :
#     stack.pop()

# print(''.join(stack))


import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
data = list(input().strip())

stack = []
count = 0

for x in data :

    while len(stack) > 0 and stack[-1] < x :
        if count == m :
            break
        else :
            stack.pop()
            count += 1

    stack.append(x)

for i in range(m - count) :
    stack.pop()

print(''.join(stack))