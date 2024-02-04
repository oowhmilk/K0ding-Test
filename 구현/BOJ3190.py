import sys
input = sys.stdin.readline

from collections import deque

n = int(input()) # 보드 크기 n * n
k = int(input()) # 사과 개수

apple_loc = []
for _ in range(k) : # 사과 위치
    apple_loc.append(list(map(int, input().split(' '))))

change = []
l = int(input()) # 방향 전환 횟수
for _ in range(l) :
    dis, direct = input().split()
    dis = int(dis)
    change.append((dis, direct))

board = [[0 for _ in range(n)] for _ in range(n)] # 보드 만들기

dx = [0, 1, 0, -1] # x 이동 방향
dy = [1, 0, -1, 0] # y 이동 방향
move = 0 # 현재 이동 방향

head_x, head_y = 0, 0 # 뱀 머리 위치
tail_x, tail_y = 0, 0 # 뱀 꼬리 위치
time = 0

que = deque()
que.append((0,0))

while(1) :
    time += 1 # 시간 증가

    # 머리 새 위치
    new_head_x = head_x + dx[move]
    new_head_y = head_y + dy[move]

    # 꼬리 새 위치
    new_tail_x = tail_x + dx[move]
    new_tail_y = tail_y + dy[move]

    for i in range(len(change)) : # 방향 바꾸기 
        if change[i][0] == time :
            if change[i][1] == 'L' :
                move = (move + 3) % 4
            if change[i][1] == 'D' :
                move = (move + 5) % 4

    if new_head_x >= n or new_head_y >= n or new_head_x < 0 or new_head_y < 0: # 보드 크기 넘어간 경우
        break

    if (new_head_x, new_head_y) in que:
        break

    apple = False
    for i in range(len(apple_loc)) :
        if apple_loc[i][0] - 1 == new_head_x and apple_loc[i][1] - 1 == new_head_y : # 사과가 존재하는 경우
            apple = True
            apple_loc.pop(i)
            break # 이전 꼬리 위치 그대로 남기고 머리만 옮기기

    if apple :
        head_x = new_head_x
        head_y = new_head_y
        board[head_x][head_y] = 1 # 새로 이동할 머리 위치 1로 바꿔주기
        que.append((head_x, head_y))
    else :
        board[tail_x][tail_y] = 0 # 이전 꼬리 위치 0 으로 바꿔주기
        que.popleft()
        tail_x = new_tail_x
        tail_y = new_tail_y

        head_x = new_head_x
        head_y = new_head_y
        board[head_x][head_y] = 1 # 새로 이동할 머리 위치 1로 바꿔주기
        que.append((head_x, head_y))

print(time)

# from collections import deque

# def simulate_game(n, k, apples, l, moves):
#     # 보드 초기화: 0은 빈 칸, 1은 뱀, 2는 사과
#     board = [[0] * n for _ in range(n)]
#     for apple in apples:
#         board[apple[0] - 1][apple[1] - 1] = 2

#     # 초기 뱀 설정: 뱀은 (0, 0)에서 시작하며, 길이는 1
#     snake = deque([(0, 0)])
#     board[0][0] = 1  # 뱀의 위치를 1로 표시
    
#     # 이동 방향 초기화: 오른쪽(0), 아래(1), 왼쪽(2), 위(3)
#     dx = [0, 1, 0, -1]
#     dy = [1, 0, -1, 0]
#     direction = 0  # 초기 방향은 오른쪽
    
#     time = 0  # 게임이 시작된 후 흐른 시간
#     move_index = 0  # 다음에 수행할 방향 변환

#     while True:
#         time += 1
#         head_x, head_y = snake[-1]
#         new_x = head_x + dx[direction]
#         new_y = head_y + dy[direction]

#         # 벽 또는 자기 자신의 몸과 충돌하는 경우 게임 종료
#         if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or board[new_x][new_y] == 1:
#             return time

#         # 사과가 없는 경우 꼬리 이동
#         if board[new_x][new_y] != 2:
#             tail_x, tail_y = snake.popleft()
#             board[tail_x][tail_y] = 0

#         # 뱀의 머리를 새 위치로 이동
#         snake.append((new_x, new_y))
#         board[new_x][new_y] = 1

#         # 방향 전환 처리
#         if move_index < l and time == moves[move_index][0]:
#             direction = (direction + (1 if moves[move_index][1] == 'D' else -1)) % 4
#             move_index += 1

# # 입력 예시
# n = int(input()) # 보드 크기 n * n
# k = int(input()) # 사과 개수

# apples = []
# for _ in range(k) : # 사과 위치
#     apples.append(list(map(int, input().split(' '))))

# moves = []
# l = int(input()) # 방향 전환 횟수
# for _ in range(l) :
#     dis, direct = input().split()
#     dis = int(dis)
#     moves.append((dis, direct))
    
    
# # 시뮬레이션 실행 및 결과 출력
# print(simulate_game(n, k, apples, l, moves))
