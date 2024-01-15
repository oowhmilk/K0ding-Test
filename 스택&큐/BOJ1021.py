from collections import deque

n, m = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

deq = deque()

result = 0

for x in range(n) :
    deq.append(x)


for i in range(m) :
    check = data[i] - 1

    index = -1
    for x in range(n) :
        if check == deq[x] :
            index = x
            break

    length = len(deq)

    left = index
    right = length - index
    min_count = min(left, right)

    for _ in range(min_count) :
        if left == min_count :
            left_pop = deq.popleft()
            deq.append(left_pop)
        else :
            right_pop = deq.pop()
            deq.appendleft(right_pop)
    
    deq.popleft()
    result += min_count


print(result)
