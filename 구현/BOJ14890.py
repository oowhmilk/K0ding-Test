import sys
input = sys.stdin.readline

def dec_check(i, j) :
    global block

    count = 0
    for k in range(1, l + 1) :
        if j - k < 0 :
            return False
        else :
            if arr[i][j] - 1 == arr[i][j - k] :
                if block[j - k] == 0 :
                    block[j - k] = 1
                    count += 1
                else :
                    return False
            else :
                return False
                
    return True

def inc_check(i, j) :
    global block

    count = 0
    for k in range(l) :
        if n <= j + k :
            return False
        else :
            if arr[i][j - 1] - 1 == arr[i][j + k] :
                if block[j + k] == 0 :
                    block[j + k] = 1
                    count += 1
                else :
                    return False
            else :
                return False
                
    return True


n, l = map(int, input().split(' '))
arr = []

for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

result = 0
for i in range(n) :
    before = arr[i][0]
    block = [0] * n

    success = True
    for j in range(1, n) :

        if arr[i][j] == before : # 다음 값이 같은 경우
            before = arr[i][j]
            continue

        elif before + 1 == arr[i][j] : # 다음 값이 큰 경우
            before = arr[i][j]
            if dec_check(i, j) :
                continue
            else :
                success = False
                break

        elif before - 1 == arr[i][j] : # 다음 값이 작은 경우
            before = arr[i][j]
            if inc_check(i, j) :
                continue
            else :
                success = False
                break

        else :
            success = False
            break

    if success :
        result += 1



def transpose(matrix) :
    row_count = len(matrix)
    column_count = len(matrix[0])

    new_arr = [[0] * row_count for i in range(column_count)]
    for i in range(column_count) :
        for j in range(row_count) :
            new_arr[i][j] = matrix[j][i]

    return new_arr

arr = transpose(arr)
for i in range(n) :
    before = arr[i][0]
    block = [0] * n

    success = True
    for j in range(1, n) :

        if arr[i][j] == before : # 다음 값이 같은 경우
            before = arr[i][j]
            continue

        elif before + 1 == arr[i][j] : # 다음 값이 큰 경우
            before = arr[i][j]
            if dec_check(i, j) :
                continue
            else :
                success = False
                break

        elif before - 1 == arr[i][j] : # 다음 값이 작은 경우
            before = arr[i][j]
            if inc_check(i, j) :
                continue
            else :
                success = False
                break

        else :
            success = False
            break

    if success :
        result += 1

print(result)