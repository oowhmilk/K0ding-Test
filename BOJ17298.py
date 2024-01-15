n = int(input())
data = list(map(int, input().split(' ')))

stack = []
NGE = [-1] * n

for i in range (len(data)) :
    check = data[i]
    
    if len(stack) == 0 or stack[-1][0] >= check:
        stack.append((check, i))
    else :
        while len(stack) > 0 :
            previous, index = stack.pop()
            if previous >= check :
                stack.append((previous, index))
                break
            else :
                NGE[index] = check
        stack.append((check, i))
    
for x in NGE:
    print(x, end = ' ')
