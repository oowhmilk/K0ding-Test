import sys
input = sys.stdin.readline

def move() :
    arr = [[[] for _ in range(n)] for _ in range(n)]
    
    for i in range(len(fire)) :
        r, c, m, s, d = fire[i]
        dx, dy = dir[d]
        nx = (r + dx * s) % n
        ny = (c + dy * s) % n

        arr[nx][ny].append((m, s, d))
        fire[i] = (nx, ny, m, s, d)

    return arr
    
def split() :
    new_fire = []
    removed = set()

    for i in range(n) :
        for j in range(n) :
            if len(arr[i][j]) >= 2 :
                removed.add((i, j))
                sum_m = 0
                sum_s = 0
                even = True
                odd = True

                for (m, s, d) in arr[i][j] :
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0 :
                        odd = False
                    else :
                        even = False

                if odd or even : 
                    directions = [0, 2, 4, 6]
                else :
                    directions = [1, 3, 5, 7]
                
                for d in directions :
                    if sum_m // 5 > 0 :
                        ball = (i, j, sum_m // 5, sum_s // len(arr[i][j]), d)
                        new_fire.append(ball)

    return removed, new_fire

n, m, k = map(int, input().split(' '))

fire = []
for _ in range(m) :
    r, c, m, s, d = map(int, input().split(' '))
    fire.append((r - 1, c - 1, m, s, d))

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(k) :
    arr = move()
    removed, new_fire = split()
    for fir in fire :
        x, y = fir[:2]

        if (x, y) not in removed :
            new_fire.append(fir)

    fire = new_fire

answer = 0
for fir in fire :
    answer += fir[2]

print(answer)