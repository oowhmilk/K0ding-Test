# import sys
# input = sys.stdin.readline

# from collections import deque

# n = int(input())
# crane = list(map(int, input().split(' ')))

# m = int(input())
# box = list(map(int, input().split(' ')))

# # 정렬
# crane.sort()
# box.sort() 

# # 내림차순 정렬
# crane.reverse()
# box.reverse()

# if max(crane) < max(box) :
#     print(-1)
#     sys.exit()

# count = 0      
# i = 0            
# while len(box) :
#     for j in range(len(box)) :
#         if crane[i] >= box[j] : 
#             box.remove(box[j])
#             if i != n - 1 and len(box) == 0 :
#                 count += 1
#             break

#     i += 1

#     if i == n :
#         count += 1
#         i = 0 

# print(count)


import sys
input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))

m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

if crane[0] < box[0]:
    print(-1)
    sys.exit()

time = 0
while len(box) :
    for i in range(n) :
        for j in range(len(box)) :
            if crane[i] >= box[j] :
                box.remove(box[j])
                break

    time += 1

print(time)