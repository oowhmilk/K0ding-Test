import sys
input = sys.stdin.readline

import heapq

n = int(input())
arr = [0] * 10001

for i in range(n) :
    data = int(input())
    arr[data] += 1

for i in range(10001) :
    for j in range(arr[i]) :
        print(i)