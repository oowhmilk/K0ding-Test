n = int(input())

stack = []
stack.append(0)

for i in range(n) :
    data = int(input())
    top = stack.pop()

    if top < data:
        stack.append(top)
        for j in range(top + 1, data + 1):
            stack.append(j)
            print("+")

    top = stack.pop()
    if top == data :
        print("-")
