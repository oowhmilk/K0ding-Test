n = int(input())

stack = []
result = []
plus_count = 0
minus_count = 0

max = 0
stack.append(0)

for i in range(n) :
    data = int(input())
    top = stack.pop()
    stack.append(top)

    if top < data:
        for j in range(max + 1, data + 1):
            stack.append(j)
            result.append("+")
            plus_count += 1
            max = j

    top = stack.pop()
    if top == data :
        result.append("-")
        minus_count += 1

if plus_count == minus_count :
    for i in range(len(result)) :
        print(result[i])
else :
    print("NO")


## 풀이
# n = int(input())

# count = 1
# stack = []
# result = []

# for i in range(1, n + 1): # 데이터 개수만큼 반복
#     data = int(input())
    
#     while count <= data: # 입력 받은 데이터에 도달할 때까지 삽입
#         stack.append(count)
#         count += 1
#         result.append('+')
    
#     if stack[-1] == data: # 스택의 최상위 원소가 데이터와 같을 때 출력
#         stack.pop()
#         result.append('-')
#     else: # 불가능한 경우
#         print('NO')
#         exit(0)

# print('\n'.join(result)) # 가능한 경우