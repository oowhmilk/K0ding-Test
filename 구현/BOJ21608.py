import sys
input = sys.stdin.readline

def find_like(x, y, like) :
    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    count = 0
    for dx, dy in dir :
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] in like :
            count += 1

    return count

def find_zero(x, y) :
    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    count = 0
    for dx, dy in dir :
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 :
            count += 1

    return count

n = int(input())

arr = [[0] * n for _ in range(n)]

save = [0] * (n ** 2 + 1)
for _ in range(n ** 2) :
    now, one, two, three, four = map(int, input().split(' '))
    like = [one, two, three, four]

    save[now] = like

    like_count = -1
    like_count_arr = []
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 0 :
                count = find_like(i, j, like)

                if like_count < count : 
                    like_count = count
                    like_count_arr = []
                    like_count_arr.append((i, j))
                elif like_count == count :
                    like_count_arr.append((i, j))

    zero_count = -1
    zero_count_arr = []
    for x, y in like_count_arr :
        count = find_zero(x, y)

        if zero_count < count :
            zero_count = count
            zero_count_arr = []
            zero_count_arr.append((x, y))
        elif zero_count == count :
            zero_count_arr.append((x, y))

    zero_count_arr.sort()

    select_x, select_y = zero_count_arr[0]
    arr[select_x][select_y] = now

answer = 0
for i in range(n) :
    for j in range(n) :
        count = find_like(i, j, save[arr[i][j]])

        if count == 0 :
            answer += 0
        elif count == 1 :
            answer += 1
        elif count == 2 :
            answer += 10
        elif count == 3 :
            answer += 100
        elif count == 4 :
            answer += 1000

print(answer)