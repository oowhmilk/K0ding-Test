import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))
sorted_arr = set(arr)
sorted_arr = sorted(sorted_arr)

data = {}
for i in range(len(sorted_arr)) :
    data[sorted_arr[i]]= i

for x in arr :
    print(data[x], end = ' ')