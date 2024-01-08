case = int(input())

for _ in range(case) :
    
    result = []
    count = 0

    string = input()

    for i in range(len(string)) :
        
        if string[i] == '-' : # backspace 일 경우 지우기
            if count > 0 :
                count -= 1
                result.pop(count)
                print(result)
        
        elif string[i] == '<' :
            if count != 0 :
                count -= 1
            elif count == 0 :
                count = 0
            print(result)
        
        elif string[i] == '>' :
            if count < len(result) :
                count += 1
            print(result)

        else :
            result.insert(count, string[i])
            count += 1
            print(result)

    print(''.join(result))

