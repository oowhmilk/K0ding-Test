import sys
input = sys.stdin.readline

import heapq

t = int(input()) 

for _ in range(t) :
    k = int(input())

    normal_heap = []
    abs_heap = []
    heap_len = 0

    for _ in range(k) :
        str = input().split()
        command, value = str[0], int(str[1])
        
        if command == 'I' : # 값 input
            
            if len(abs_heap) == 0 or len(normal_heap) == 0 :
                abs_heap = []
                normal_heap = []
            
            minus = value * (-1)
            heapq.heappush(normal_heap, value)
            heapq.heappush(abs_heap, (-value))
            heap_len += 1

        else : # 값 뽑기
            if value == 1 : # 최대값 뽑기
                if heap_len != 0 :
                    heapq.heappop(abs_heap)
                    heap_len -= 1
            else : # 최소값 뽑기
                if heap_len != 0 :
                    heapq.heappop(normal_heap)
                    heap_len -= 1

    if heap_len == 0:
        print('EMPTY')
    elif heap_len == 2 :
        max = heapq.heappop(abs_heap)
        min = heapq.heappop(abs_heap)
        print(-1 * max, -1 * min)
    elif heap_len == 1 :
        max = heapq.heappop(abs_heap)
        min = heapq.heappop(normal_heap)
        print(-1 * max, -1 * max)
    else : 
        max = heapq.heappop(abs_heap)
        min = heapq.heappop(normal_heap)
        print(-1 * max, min)