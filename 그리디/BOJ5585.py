import sys
input = sys.stdin.readline

n = int(input())
change = 1000 - n 

count = 0
for i in [500,100,50,10,5,1] :
    count += change // i
    change %= i

print(count)