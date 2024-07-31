import sys
input = sys.stdin.readline

# def calcuate_r() :
#     global arr
#     new_arr = [[] for _ in range(len(arr))]

#     for i in range(len(arr)) :
#         dic = {}
#         for j in range(len(arr[i])) :
#             if arr[i][j] == 0 :
#                 continue
#             if arr[i][j] not in dic :
#                 dic[arr[i][j]] = 1
#             else :
#                 dic[arr[i][j]] += 1

#         dic = dict(sorted(dic.items(), key = lambda x : (x[1], x[0])))

#         for key, value in dic.items() :
#             new_arr[i].append(key)
#             new_arr[i].append(value)

#     max_row = 0
#     for i in range(len(new_arr)) :
#         max_row = max(max_row, len(new_arr[i]))

#     for i in range(len(new_arr)) :
#         gap = max_row - len(new_arr[i])
#         new_arr[i] += [0] * gap
#         new_arr[i] = new_arr[i][:100]

#     arr = new_arr

# r, c, k = map(int, input().split(' '))
# arr = []
# for _ in range(3) :
#     arr.append(list(map(int, input().split(' '))))

# time = 0
# result = False
# while time < 100 :

#     row_count = len(arr) # 행의 개수
#     column_count = len(arr[0]) # 열의 개수

#     if row_count >= r and column_count >= c :
#         if arr[r-1][c-1] == k :
#             result = True
#             break

#     if row_count >= column_count :
#         calcuate_r()
#     else :
#         transpose()
#         calcuate_r()
#         transpose()

#     time += 1

# if result :
#     print(time)
# else :
#     print(-1)


def sort_row(row) :
    counter = dict()
    for x in row :
        if x == 0 :
            continue
        if x not in counter :
            counter[x] = 1
        else : 
            counter[x] += 1

    sorted_counter = sorted(counter.items(), key = lambda x : (x[1], x[0]))

    result = []
    for val, cnt in sorted_counter :
        result += [val, cnt]

    return result


def transpose(matrix) :
    row_count = len(matrix)
    column_count = len(matrix[0])

    new_arr = [[0] * row_count for i in range(column_count)]
    for i in range(column_count) :
        for j in range(row_count) :
            new_arr[i][j] = matrix[j][i]

    return new_arr

def process(matrix, operator) :
    if operator == 'C' :
        matrix = transpose(matrix)

    max_length = 0
    for i in range(len(matrix)) :
        matrix[i] = sort_row(matrix[i])
        max_length = max(max_length, len(matrix[i]))

    for i in range(len(matrix)) :
        gap = max_length - len(matrix[i])
        matrix[i] += [0] * gap
        matrix[i] = matrix[i][:100]

    if operator == 'C' :
        matrix = transpose(matrix)

    return matrix

r, c, k = map(int, input().split(' '))
matrix = []
for _ in range(3) :
    matrix.append(list(map(int, input().split(' '))))

t = 0
while True :
    row_length = len(matrix)
    column_length = len(matrix[0])

    if row_length >= r and column_length >= c :
        if matrix[r - 1][c - 1] == k :
            print(t)
            break

    if t == 100 :
        print(-1)
        break

    if row_length >= column_length :
        matrix = process(matrix, 'R')
    else :
        matrix = process(matrix, 'C')

    t += 1