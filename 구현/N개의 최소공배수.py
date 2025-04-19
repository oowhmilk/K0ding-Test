import math 

def solution(arr):
    answer = 0
    
    n = arr[0]
    for i in range(len(arr)) :
        n = n * arr[i] // math.gcd(n, arr[i])
    
    answer = n
    return answer