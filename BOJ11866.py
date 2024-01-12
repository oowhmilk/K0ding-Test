from collections import deque 

n, k = map(int, input().split(' '))

deq = deque()
result = []

for i in range(n) :
    deq.append(i + 1)

while len(deq) > 0 :

    for i in range(k - 1) :
        num = deq.popleft()
        deq.append(num)
    
    result.append(deq.popleft())

print('<', end = ' ')
for i in range(len(result)) : 
    if i < len(result) - 1 :
        print(result[i], end = ', ')
    else :
        print(result[i], end = '')
print('>')