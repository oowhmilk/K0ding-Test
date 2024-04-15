arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 시계 방향 90도
arr_90 = list(map(list, zip(*arr[::-1])))
print(arr_90)

#시계 방향 180도
arr_180 = [a[::-1] for a in arr[::-1]]
print(arr_180)

# 시계 방향 270도
arr_270 = [x[::-1] for x in list(map(list, zip(*arr[::-1])))[::-1]]
print(arr_270)


## 부분회전
# 7X7 배열
arr = [[7 * j + i for i in range(1, 8)] for j in range(7)]
new_arr = [[0] * 3 for _ in range(3)]
sy, sx = 2, 2
length = 3

for i in range(3) :
    for j in range(3) :
        new_arr[i][j] = arr[sx + i][sy + j]

check_arr = [[0] * 3 for _ in range(3)]
for i in range(3) :
    for j in range(3) :
        check_arr[j][length - 1 - i] = new_arr[i][j]

for i in range(len(check_arr)) :
    for j in range(len(check_arr)) :
        arr[i + 2][j + 2] = check_arr[i][j]

print(arr)


## 순열
arr = [1, 2, 3, 4]
visited = [0] * len(arr) 

def permutations(n, new_arr) :
    global arr

    if len(new_arr) == n :
        print(new_arr)
        return
    for i in range(len(arr)) :
        if not visited[i] :
            visited[i] = 1
            permutations(n, new_arr + [arr[i]])
            visited[i] = 0

permutations(2, [])

## 중복 순열
arr = [1, 2, 3, 4]
def product(n, new_arr):
    global arr
    # 순서 상관 0, 중복 0
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(len(arr)):
        product(n, new_arr + [arr[i]])

product(2, [])


## 조합
arr = [1, 2, 3, 4]

def combinations(n, new_arr, c) :
    global arr

    if len(new_arr) == n :
        print(new_arr)
        return
    
    for i in range(c, len(arr)) :
        combinations(n, new_arr + [arr[i]], i + 1)

combinations(2, [], 0)

## 중복 조합
arr = [1, 2, 3, 4]

def combinations_with_replacement(n, new_arr, c):
    # 순서 상관 X, 중복
    if len(new_arr) == n:
        print(new_arr)
        return
    for i in range(c, len(arr)):
        combinations(n, new_arr + [arr[i]], i)


combinations_with_replacement(2, [], 0)


## 중력
