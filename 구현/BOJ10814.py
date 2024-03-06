import sys
input = sys.stdin.readline

n = int(input())
arr =[]

for _ in range(n) :
    input_data = input().split(' ')
    arr.append((int(input_data[0]), input_data[1]))

arr = sorted(arr, key = lambda x: x[0])

for i in arr :
    print(i[0], i[1], end ='')