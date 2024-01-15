from itertools import permutations

n, m = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))

permutations_arr = list(permutations(arr, 3))

max_value = -1

for i in range(len(permutations_arr)) :
    a, b, c = permutations_arr[i]
    if max_value < (a + b + c) and (a + b + c) <= m:
        max_value = (a + b + c)

print(max_value)


## 풀이
# n, m = list(map(int, input().split(' ')))
# arr = list(map(int, input().split(' ')))

# result = 0
# length = len(arr)

# count = 0
# for i in range(0, length) :
#     for j in range(i + 1, length) :
#         for k in range(j + 1, length) :
#             sum_value = arr[i] + arr[j] + arr[k]
#             if sum_value <= m:
#                 result = max(result, sum_value)

# print(result)