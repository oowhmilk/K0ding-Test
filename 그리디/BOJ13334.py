# 길이가 d 인 철로 선분을 왼쪽에서 오른쪽으로 이동
# 모든 선분의 "끝"으로 오름차순 정렬
# 해당 선분이 d 보다 길면 무시
# 해당 선분이 끝점에 닿도록 철로 선분을 이동시키고, heap 에 시작점을 삽입
# 철로 선분이 이동함에 따라서, 철로를 벗어난 시작점을 heap 에서 추출
# 현재 heap 의 크기 를 계산

import sys
input = sys.stdin.readline

import heapq

n = int(input()) 
lines = []

for _ in range(n) :
    h, o = map(int, input().split(' '))
    start = 0
    finsih = 0
    if h > o :
        start = o
        finish = h
    else :
        start = h
        finish = o
    
    lines.append((start, finish))

lines.sort(key = lambda x : x[1])

d = int(input())

heap = []
cur = 0 # 철로 선분의 끝점 => 철로는 오른쪽으로 조금씩 이동
result = 0 

for line in lines :
    start, end = line
    if end - start > d :
        continue
    cur = end # 철로 오른쪽으로 이동
    heapq.heappush(heap, start)

    while len(heap) > 0 :
        start = heapq.heappop(heap) # 가장 왼쪽에 있는 시작점 확인

        if cur - start > d :  # 철로를 벗어났으면 그대로 
            continue
        else : 
            heapq.heappush(heap, start) # 철로를 벗어나지 않으면 다시 넣어주고 
            break

    result = max(result, len(heap))

print(result)