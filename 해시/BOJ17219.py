import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

dict = {}
for _ in range(n) :
    address, password = input().strip().split(' ')
    dict[address] = password

for _ in range(m) : 
    address = input().strip()
    print(dict[address])