from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * n for _ in range(n)]

apple_count = int(input())
apple = []
for _ in range(apple_count) :
    x, y = map(int, input().split(' '))
    apple.append((x - 1, y - 1))

change_dir = {}
for _ in range(int(input())) :
    time, change = input().strip().split(' ')
    change_dir[int(time)] = change

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
now_dir = 1
snake = deque()
snake.append((0, 0))
arr[0][0] = 1

time = 0
while True :
    time += 1

    x, y = snake.popleft()

    # 머리 이동
    dx, dy = dir[now_dir]

    nx = x + dx
    ny = y + dy 

    # 게임 끝남 여부 확인
    end = False
    exist_apple = False
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0 :
        end = True
        if (nx, ny) in apple :
            exist_apple = True
            apple.remove((nx, ny))
            
            snake.appendleft((x, y))
            snake.appendleft((nx, ny))
        else :
            snake.appendleft((x, y))
            snake.appendleft((nx, ny))
    
    if not end :
        print(time)
        break

    if exist_apple :
        x, y = snake[0]
        arr[x][y] = 1
    else :
        x, y = snake[0]
        arr[x][y] = 1

        del_x, del_y = snake.pop()
        arr[del_x][del_y] = 0

    if time in change_dir :
        if change_dir[time] == 'D' :
            now_dir = ((now_dir + 1) + 4) % 4
        elif change_dir[time] == 'L' :
            now_dir = ((now_dir - 1) + 4) % 4