# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split(' '))
# arr = list(map(int, input().split(' ')))

# check = [] # 짝수 : 0, 홀수 : 1
# for x in arr :
#     check.append(x % 2) 

# if len(check) == 1 :
#     if check[0] == 0 :
#         print(1)
#         sys.exit()
#     else :
#         print(0)
#         sys.exit()

# left = 0
# right = 1
# max_size = 0

# if check[left] == 0 :
#     cnt = 0
# else :
#     cnt = 1

# while left < right and right < n:
    
#     if cnt == k :
#         if check[right] == 0 :
#             max_size = max(max_size, right - left - cnt + 1) 
#         else :
#             max_size = max(max_size, right - 1 - left - cnt + 1) 
        
#         left += 1
#         if check[left] == 0 :
#             cnt = 0
#         else :
#             cnt = 1
        
#         right = left + 1
#         continue

#     if check[right] == 0 :
#         right += 1
#     else :
#         cnt += 1
#         right += 1

# max_size = max(max_size, right - 1 - left - cnt + 1) 
# print(max_size)


import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

end = 0
answer = 0
tmp = 0
odd = 0

for start in range(n) :
    while odd <= k and end < n :
        if arr[end] % 2 :
            odd += 1
        else :
            tmp += 1

        end += 1

        if start == 0 and end == n :
            answer = tmp
            break

    if odd == k + 1 :
        answer = max(answer, tmp)

    if arr[start] % 2 :
        odd -= 1
    else :
        tmp -= 1

print(answer)