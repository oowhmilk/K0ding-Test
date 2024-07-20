# import sys
# input = sys.stdin.readline

# n = int(input())

# lines = []
# for _ in range(n):
#     lines.append(tuple(map(int, input().split())))

# lines.sort()

# left = lines[0][0]
# right = lines[0][1]
# ans = 0

# for i in range(1, n) :
#     if right > lines[i][1] :
#         continue

#     elif lines[i][0] <= right < lines[i][1] :
#         right = lines[i][1]

#     elif  right < lines[i][0] :
#         ans += right - left
#         left = lines[i][0]
#         right = lines[i][1]

# ans += right - left

# print(ans)


# import sys
# input = sys.stdin.readline

# n = int(input())

# arr = []
# for i in range(n) :
#     x, y = map(int, input().split(' '))
#     arr.append((x, y))

# arr = sorted(arr)

# before_x = arr[0][0]
# before_y = arr[0][1]

# result = 0
# for i in range(1, len(arr)) :
#     if arr[i][1] < before_y :
#         continue
#     elif arr[i][0] <= before_y < arr[i][1]:
#         before_y = arr[i][1]
#     elif before_y < arr[i][0] : 
#         result += (before_y - before_x)
#         before_x = arr[i][0]
#         before_y = arr[i][1]

# result += (before_y - before_x)

# print(result)


import sys
input = sys.stdin.readline

import heapq

n = int(input())

arr = []
for _ in range(n) : 
    start, end = map(int, input().split(' '))
    heapq.heappush(arr, (start, end))

result = []
start, end = heapq.heappop(arr)
result.append((start, end))

for _ in range(len(arr)) :
    
    new_start, new_end = heapq.heappop(arr)
        
    if new_start <= end :
        if new_end <= end :
            continue
        else :
            result.pop(-1)
            result.append((start, new_end))
            end = new_end
    elif end < new_start :
        result.append((new_start, new_end))
        start = new_start
        end = new_end
    
count = 0
for i in range(len(result)) :
    count += result[i][1] - result[i][0]
print(count)