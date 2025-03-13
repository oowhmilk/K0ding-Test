import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def calculate(sum, index, num, sign, string) :
    if index == n : 
        sum = sum + (sign * num)
        if sum == 0 :
            print(string)
    else :
        # ' ' 
        calculate(sum, index + 1, num * 10 + (index + 1), sign, string + ' ' + str(index + 1)) 
        # +
        calculate(sum + sign * num, index + 1, index + 1, 1, string + '+' + str(index + 1))
        # -
        calculate(sum + sign * num, index + 1, index + 1, -1, string + '-' + str(index + 1))


for _ in range(int(input())) :
    n = int(input())

    calculate(0, 1, 1, 1, "1") 
    print()