import sys
input = sys.stdin.readline

n = int(input())
time = 0
count = 0
i = 0

while n != count :

    i += 1
    count += i
    if n < count :
        count -= i
        i = 0
    else :
        time += 1

print(time)