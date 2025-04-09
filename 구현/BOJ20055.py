from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split(' '))
belt = deque(map(int, input().split(' ')))
robot = deque([False] * n)

answer = 0
while True :

    answer += 1

    # 벨트 회전
    belt.rotate(1)
    robot.rotate(1)

    # n 번째에 있는 로봇 내리기
    robot[n - 1] = False

    # 로봇 이동하기
    for i in range(len(robot) - 2, -1, -1) :
        if robot[i] == True and belt[i + 1] >= 1 and robot[i + 1] == False :
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1

    # n 번째에 있는 로봇 내리기
    robot[n - 1] = False

    # 로봇 올리기
    if robot[0] == False and belt[0] >= 1:
        robot[0] = True
        belt[0] -= 1

    # 내구도 0 인 개수 확인하기
    count = 0
    for i in range(len(belt)) :
        if belt[i] == 0 :
            count += 1

    if count >= k :
        break

print(answer)