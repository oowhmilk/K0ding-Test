case = int(input())

result = []

for _ in range(case) :
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))

    queue = [(i, idx) for idx, i in enumerate(queue)]
    count = 0

    while True :
        if queue[0][0] == max([i[0] for i in queue]) :
            count += 1
            if queue[0][1] == m :
                result.append(count)
                break
            else :
                queue.pop(0)

        else :
            queue.append(queue.pop(0))

for i in range(len(result)) :
    print(result[i])

## 풀이 
# test_case = int(input())

# for _ in range(test_case):
#     n, m = list(map(int, input().split(' ')))
#     queue = list(map(int, input().split(' ')))
#     queue = [(i, idx) for idx, i in enumerate(queue)]
#     count = 0

#     while True:
#         if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
#             count += 1
#             if queue[0][1] == m:
#                 print(count)
#                 break
#             else:
#                 queue.pop(0) 
#         else:
#             queue.append(queue.pop(0))