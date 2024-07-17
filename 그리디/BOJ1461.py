# import sys
# input = sys.stdin.readline

# n, m  = map(int, input().split(' '))
# books = list(map(int, input().split(' ')))
# books.sort()

# minus = []
# plus = []

# for i in range(n) : 
#     if books[i] < 0 :
#         minus.append(abs(books[i]))


# for i in range(n) : 
#     if books[i] > 0 :
#         plus.append(books[i])

# if len(minus) == 0 :
#     max_distance = max(plus)
# elif len(plus) == 0 :
#     max_distance  = max(minus)
# else :
#     max_distance = max(abs(minus[0]), plus[len(plus) - 1])

# result = 0
# i = 0
# while i < len(minus) :
#     if minus[i] == max_distance :
#         result += max_distance
#     else :
#         result += (minus[i] * 2)

#     if len(minus) - i - m >= 0 :
#         i += m
#     else :
#         break


# plus.reverse()
# i = 0
# while i < len(plus) :
#     if plus[i] == max_distance :
#         result += max_distance
#     else :
#         result += (plus[i] * 2)

#     if len(plus) - i - m >= 0 :
#         i += m
#     else :
#         break

# print(result)

# import heapq

# n, m - map(int, input().split(' '))
# arr = list(map(int, input().split(' ')))

# positive = []
# negative = []

# largest = max(max(arr), -min(arr))

# for i in arr :
#     if i > 0 :
#         heapq.heappush(positive, -i)
#     else :
#         heapq.heappush(negative, i)

# result = 0

# while positive :
#     result += heapq.heappop(positive) 
#     for _ in range(m - 1) :
#         if positive :
#             heapq.heappop(positive)

# while negative :
#     result += heapq.heappop(negative)
#     for _ in range(m - 1) :
#         if negative :
#             heapq.heappop(negative)

# print(-result * 2 - largest)


import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
arr.sort()

minus = []
plus = []

for x in arr :
    if x < 0 :
        minus.append(abs(x))
    else :
        plus.append(x)

minus.sort(reverse=True)
plus.sort(reverse=True)

result = 0

i = 0
while i < len(minus) :
    result += minus[i]
    i += m

j = 0
while j < len(plus) :
    result += plus[j]
    j += m

max_distance = 0
if len(minus) == 0 and len(plus) != 0 :
    max_distance = plus[0]
elif len(minus) != 0 and len(plus) == 0 :
    max_distance = minus[0]
else :
    max_distance = max(minus[0], plus[0])

result = result * 2 - max_distance

print(result)