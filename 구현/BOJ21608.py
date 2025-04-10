import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * n for _ in range(n)]

input_arr = []
for _ in range(n ** 2) :
    input_arr.append(list(map(int, input().split(' '))))

for data in input_arr :

    student = data[0]

    # 비어있는 칸 중에 좋아하는 학생 몇명있는지 확인
    score = [[0] * n for _ in range(n)]
    
    for x in range(n) :
        for y in range(n) :
            count = 0
            for k in range(1, len(data)) :

                check = data[k]
                dir = {(-1, 0), (0, 1), (0, -1), (1, 0)}
                for dx, dy in dir :
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == check :
                        count += 1

            score[x][y] = count

    # 비어있는 칸 중에 좋아하는 학생 수의 큰 값을 찾기
    empty = 0
    input_x = -1
    input_y = -1

    max_score = -1
    for i in range(n) :
        for j in range(n) :
            if max_score < score[i][j] and arr[i][j] == 0 :
                max_score = score[i][j]
                input_x = i
                input_y = j

    
    for x in range(n) :
        for y in range(n) :

            count = 0
            if max_score == score[x][y] and arr[x][y] == 0 :
                dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}
                for dx, dy in dir :
                    nx = x + dx
                    ny = y + dy 

                    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 :
                        count += 1

            if count > empty :
                empty = count
                input_x = x
                input_y = y

    arr[input_x][input_y] = student



ans = 0
for data in input_arr :
    input = data[0]

    for i in range(n) :
        for j in range(n) :

            x = i
            y = j
            count = 0

            if input == arr[i][j] :
                
                for k in range(1, len(data)) : # 넣을려는 값들의 좋아하는 값들이 주변에 있는지 확인하기
                
                    check = data[k] # 좋아하는 값
                    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
                    for dx, dy in directions :
                        nx = x + dx
                        ny = y + dy

                        if nx < 0 or n <= nx or ny < 0 or n <= ny :
                            continue

                        if check == arr[nx][ny] :
                            count += 1

                
            if count == 0 : 
                ans += 0
            elif count == 1:
                ans += 1
            elif count == 2:
                ans += 10
            elif count == 3:
                ans += 100
            elif count == 4:
                ans += 1000

print(ans)