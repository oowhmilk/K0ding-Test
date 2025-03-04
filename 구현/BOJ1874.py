import sys
input = sys.stdin.readline

n = int(input())

count = 1
stack = []
result = []

for i in range(n) :
    data = int(input())

    while count <= data :
        stack.append(count)
        count += 1
        result.append('+')

    if stack[-1] == data :
        stack.pop()
        result.append('-')
    else :
        print("NO")
        sys.exit()

for x in result :
    print(x)