import sys
input = sys.stdin.readline

from collections import deque
import heapq

def check_fish() : # 물고기 존재 여부
    for i in range(n) :
        for j in range(n) :
            if 1 <= arr[i][j] <= 6 :
                fish.append(arr[i][j])

def can_eat() : # 현재 가장 작은 물고기 크기가 상어 크기 보다 크거나 같은 경우
    if shark_size <= min(fish) : 
        return False
    
    return True

def bfs(x, y, distance) : # 먹이 위치 찾기

    visited[x][y] = True
    q = deque()
    q.append((x, y, distance))

    while q :
        x, y, distance = q.popleft()
        
        if 0 < arr[x][y] < shark_size :
            heapq.heappush(heap, (distance, x, y))
            # return x, y, distance

        directions = {(-1, 0), (0, -1), (1, 0), (0, 1)}
        for dx, dy in directions :
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny :
                continue

            if visited[nx][ny] == False and arr[nx][ny] <= shark_size :
                visited[nx][ny] = True
                q.append((nx, ny, distance + 1))


n = int(input())
arr = [] 

for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

fish = []
check_fish()

shark_size = 2 # 초기 상어 크기

shark_x = -1
shark_y = -1

for i in range(n) : # 현재 상어 위치 찾기
    for j in range(n) :
        if arr[i][j] == 9 :
            shark_x = i
            shark_y = j
            arr[i][j] = 0


time = 0 # 총 걸린 시간
change_size = 0 # 먹이 먹은 횟수

while True :

    if len(fish) == 0 : # 물고기를 전부 먹은 경우
        break

    if can_eat() == False : # 더 이상 먹을수 있는 물고기가 없는 경우
        break

    heap = []
    heapq.heappush(heap,(1e6, 1e6, 1e6))
    visited = [[False] * n for _ in range(n)]
    bfs(shark_x, shark_y, 0) # 먹이 위치

    if heap[0][1] == 1e6 :
        break

    data = heap[0]
    distance = data[0]
    food_x = data[1]
    food_y = data[2]

    fish.remove(arr[food_x][food_y])
    arr[food_x][food_y] = 0 # 먹이 위치 = 0
    change_size += 1 # 먹이 먹은 횟수
    time += distance # 먹이 먹으러 이동거리

    shark_x = food_x # 상어 위치 옮기기
    shark_y = food_y

    if change_size == shark_size : # 먹이 먹은 횟수 == 상어 크기 인 경우 상어 크기 +1 증가
        change_size = 0
        shark_size += 1

print(time)