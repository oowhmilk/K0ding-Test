import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n) :
    command = input().strip().split(' ') 

    if command[0] == 'push' :
        stack.append(int(command[1]))

    elif command[0] == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop(-1))

    elif command[0] == 'size' :
        print(len(stack))

    elif command[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)

    elif command[0] == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[len(stack) - 1])

