# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split(' ')))
# sorted_arr = set(arr)
# sorted_arr = sorted(sorted_arr)

# data = {}
# for i in range(len(sorted_arr)) :
#     data[sorted_arr[i]] = i

# for i in range(len(arr)) :
#     print(data[arr[i]], end = ' ')


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split(' ')))

press = set()
for x in arr :
    press.add(x)

press = sorted(press)

data = {}
for i in range(len(press)) :
    data[press[i]] = i

for i in range(len(arr)) :
    print(data[arr[i]], end = ' ')