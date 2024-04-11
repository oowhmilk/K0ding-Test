import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n ** 2) :
    arr.append(list(map(int, input().split(' '))))

grid = [[0] * n for _ in range(n)] # 실제로 넣은 배열

for data in arr :
    input = data[0]

    score = [[0] * n for _ in range(n)]

    # 새로 넣을 값 어디다 넣을지 정하기 위한 score[i][j] 마다 확인해서 점수 매기기
    for i in range(n) : 
        for j in range(n) :
            
            x = i
            y = j
            count = 0

            for k in range(1, len(data)) : # 넣을려는 값들의 좋아하는 값들이 주변에 있는지 확인하기
                
                check = data[k] # 좋아하는 값
                directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
                for dx, dy in directions :
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or n <= nx or ny < 0 or n <= ny :
                        continue

                    if check == grid[nx][ny] :
                        count += 1

            score[x][y] = count
        

    empty = 0
    input_x = -1
    input_y = -1

    # 실제로 넣을 위치 찾기
    max_score = -1
    for i in range(n) :
        for j in range(n) :
            if max_score < score[i][j] and grid[i][j] == 0:
                max_score = score[i][j]
                input_x = i
                input_y = j


    for i in range(n) :
        for j in range(n) :

            count = 0
            x = i
            y = j

            if max_score == score[x][y] and grid[x][y] == 0:
                directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
                for dx, dy in directions :
                    nx = x + dx
                    ny = y + dy

                    if nx < 0 or n <= nx or ny < 0 or n <= ny :
                        continue

                    if grid[nx][ny] == 0 : # 주변 빈칸 개수 만큼 count 증가
                        count += 1
                        
            
            if count > empty :
                empty = count
                input_x = i
                input_y = j
                

    grid[input_x][input_y] = input

ans = 0
for data in arr :
    input = data[0]

    for i in range(n) :
        for j in range(n) :

            x = i
            y = j
            count = 0

            if input == grid[i][j] :
                
                for k in range(1, len(data)) : # 넣을려는 값들의 좋아하는 값들이 주변에 있는지 확인하기
                
                    check = data[k] # 좋아하는 값
                    directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
                    for dx, dy in directions :
                        nx = x + dx
                        ny = y + dy

                        if nx < 0 or n <= nx or ny < 0 or n <= ny :
                            continue

                        if check == grid[nx][ny] :
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
                            