import sys
case = int(sys.stdin.readline())

for _ in range(case) :
    
    result = []
    count = 0

    string = sys.stdin.readline()

    for i in range(len(string)) :
        
        if string[i] == '-' : # backspace 일 경우 지우기
            if count > 0 :
                count -= 1
                result.pop(count)
        
        elif string[i] == '<' :
            if count != 0 :
                count -= 1
            elif count == 0 :
                count = 0
        
        elif string[i] == '>' :
            if count < len(result) :
                count += 1

        else :
            result.insert(count, string[i])
            count += 1

    print(''.join(result))

## 풀이
case = int(input())

for _ in range(case) :
    data = input()
    left_stack = []
    right_stack = []

    for i in data :
        if i == '-' :
            if left_stack :
                left_stack.pop()
        elif i == '<' :
            if left_stack :
                right_stack.append(left_stack.pop())
        elif i == '>' :
            if right_stack :
                left_stack.append(right_stack.pop())
        else :
            left_stack.append(i)

    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))