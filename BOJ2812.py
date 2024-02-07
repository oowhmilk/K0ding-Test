import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = input().strip()

delete = 0
stack = []

for x in data :
    while len(stack) > 0 and stack[-1] < x :
        if delete == k :
            break
        else :
            stack.pop()
            delete += 1

    stack.append(x)

for i in range(k - delete) :
    stack.pop()

print(''.join(stack))