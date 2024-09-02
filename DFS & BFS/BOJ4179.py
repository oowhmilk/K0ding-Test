from collections import deque
import sys
input = sys.stdin.readline

def move_fire() :
    
    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    while fire : 
        x, y = fire.popleft()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or r <= nx or ny < 0 or c <= ny :
                continue
            if fire_visited[nx][ny] == -1 and arr[nx][ny] != '#' :
                fire_visited[nx][ny] = fire_visited[x][y] + 1
                fire.append((nx, ny))

def move_human() :
    
    dir = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    while human :

        x, y = human.popleft()

        for dx, dy in dir :
            nx = x + dx
            ny = y + dy

            if nx < 0 or r <= nx or ny < 0 or c <= ny :
                continue
            if human_visited[nx][ny] == -1 and arr[nx][ny] != '#' :
                human_visited[nx][ny] = human_visited[x][y] + 1
                human.append((nx, ny))



    

r, c = map(int, input().split(' '))

arr = []
for _ in range(r) :
    str = input().strip()
    arr.append(list(str))

fire = deque()
fire_visited = [[-1] * c for _ in range(r)]
human = deque()
human_visited = [[-1] * c for _ in range(r)]

for i in range(r) :
    for j in range(c) :
        if arr[i][j] == 'F' :
            fire.append((i, j))
            fire_visited[i][j] = 0
        elif arr[i][j] == 'J' :
            human.append((i, j))
            human_visited[i][j] = 0

move_fire()
move_human()

result = int(1e9)

for i in range(r) :
    if human_visited[i][0] != -1 :
        if human_visited[i][0] + 1 <= fire_visited[i][0] :
            result = min(result, human_visited[i][0])
        else :
            if fire_visited[i][0] == -1 :
                result = min(result, human_visited[i][0])

    if human_visited[i][c - 1] != -1 :
        if human_visited[i][c - 1] + 1 <= fire_visited[i][c - 1] :
            result = min(result, human_visited[i][c - 1])
        else :
            if fire_visited[i][c - 1] == -1 :
                result = min(result, human_visited[i][c - 1])

for j in range(c) :
    if human_visited[0][j] != -1 :
        if human_visited[0][j] + 1 <= fire_visited[0][j] :
            result = min(result, human_visited[0][j])
        else :
            if fire_visited[0][j] == -1 :
                result = min(result, human_visited[0][j])

    if human_visited[r - 1][j] != -1 :
        if human_visited[r - 1][j] + 1 <= fire_visited[r - 1][j] :
            result = min(result, human_visited[r - 1][j])
        else :
            if fire_visited[r - 1][j] == -1 :
                result = min(result, human_visited[r - 1][j])



if result == int(1e9) :
    print("IMPOSSIBLE")
else :
    print(result + 1)