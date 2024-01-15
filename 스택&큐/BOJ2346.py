import sys 
input = sys.stdin.readline

from collections import deque

n = int(input())
arr = list(map(int, input().split()))

deq = deque()

for i in range(n) :
    deq.append((arr[i], i + 1))

result = []

check, where = deq.popleft()
result.append(where)

for _ in range(n - 1) :

    if check > 0  :
        for _ in range(check - 1) :
            num = deq.popleft()
            deq.append(num)
    else : 
        for _ in range(-check) : 
            num = deq.pop()
            deq.appendleft(num)

    check, where = deq.popleft()
    result.append(where)


for i in range(len(result)) :
    print(result[i], end=' ')