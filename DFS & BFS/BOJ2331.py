import sys
input = sys.stdin.readline

def calculate(a, p) :
    
    sum = 0
    for i in str(a):
        sum += int(i) ** p

    return sum

a, p = map(int, input().split(' '))
arr = []
arr.append(a)

while 1 :
    
    sum = 0
    sum = calculate(a, p)

    if sum not in arr :
        arr.append(sum)
    else :
        for i in range(len(arr)) :
            if arr[i] == sum :
                print(i)
                sys.exit()
    
    a = sum