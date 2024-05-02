import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

n = int(input())

def is_prime(num) :
    for i in range(2, int(num/2) + 1) :
        if num % i == 0 :
            return False
        
    return True

def DFS(number) :
    if len(str(number)) == n :
        print(number)
    else : 
        for i in range(1, 10) :
            if i % 2 == 0 : 
                continue
            if is_prime(number * 10 + i) : 
                DFS(number * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)
