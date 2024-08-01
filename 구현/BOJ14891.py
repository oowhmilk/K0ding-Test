import sys
input = sys.stdin.readline
from collections import deque

def check(n, dir) :
    # 돌리기 전에 연결 부분 이전 상태 저장    
    before_gear_1_connect = (gear_1[2], gear_2[6])
    before_gear_2_connect = (gear_2[2], gear_3[6])
    before_gear_3_connect = (gear_3[2], gear_4[6])

    if n == 1 :
        rotate(1, dir)

        if before_gear_1_connect[0] != before_gear_1_connect[1] :
            rotate(2, -dir)

            if before_gear_2_connect[0] != before_gear_2_connect[1] :
                rotate(3, dir)

                if before_gear_3_connect[0] != before_gear_3_connect[1] :
                    rotate(4, -dir)


    elif n == 2 :
        rotate(2, dir)

        if before_gear_1_connect[0] != before_gear_1_connect[1] :
            rotate(1, -dir)
        
        if before_gear_2_connect[0] != before_gear_2_connect[1] :
            rotate(3, -dir)

            if before_gear_3_connect[0] != before_gear_3_connect[1] :
                rotate(4, dir)
        


    elif n == 3 :
        rotate(3, dir)

        if before_gear_3_connect[0] != before_gear_3_connect[1] :
            rotate(4, -dir)

        if before_gear_2_connect[0] != before_gear_2_connect[1] :
            rotate(2, -dir)

            if before_gear_1_connect[0] != before_gear_1_connect[1] :
                rotate(1, dir)


    elif n == 4 :
        rotate(4, dir)

        if before_gear_3_connect[0] != before_gear_3_connect[1] :
            rotate(3, -dir)

            if before_gear_2_connect[0] != before_gear_2_connect[1] :
                rotate(2, dir)

                if before_gear_1_connect[0] != before_gear_1_connect[1] :
                    rotate(1, -dir)


def rotate(n, dir) :
    if n == 1 :
        gear_1.rotate(dir)
    elif n == 2 :
        gear_2.rotate(dir)
    elif n == 3 :
        gear_3.rotate(dir)
    elif n == 4 :
        gear_4.rotate(dir)


gear_1 = deque(input().strip())
gear_2 = deque(input().strip())
gear_3 = deque(input().strip())
gear_4 = deque(input().strip())


for _ in range(int(input())) : 

    n, dir = map(int, input().split(' ')) # dir == 1 : 시계 방향 , dir == -1 : 반시계 방향

    check(n, dir)

result = 0
result = int(gear_1[0]) * 1 + int(gear_2[0]) * 2 + int(gear_3[0]) * 4 + int(gear_4[0]) * 8

print(result)