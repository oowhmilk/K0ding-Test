import heapq
import sys
input = sys.stdin.readline

def dijkstra(start) :
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap :
        dist, now = heapq.heappop(heap)

        if distance[now] < dist :
            continue

        for i in arr[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost 
                heapq.heappush(heap, (cost, i[0]))

n, e = map(int, input().split(' '))

arr = [[] for _ in range(n + 1)]
for _ in range(e) :
    a, b, c = map(int, input().split(' '))
    arr[a].append((b, c))
    arr[b].append((a, c))

fir, sec = map(int, input().split(' '))

distance = [int(1e9)] * (n + 1)
# 1 -> fir
# 1 -> sec
dijkstra(1)
start_to_fir = distance[fir]
start_to_sec = distance[sec]

distance = [int(1e9)] * (n + 1)
# fir -> sec
# fir -> n
dijkstra(fir)
fir_to_sec = distance[sec]
fir_to_n = distance[n]

distance = [int(1e9)] * (n + 1)
# sec -> fir
# sec -> n
dijkstra(sec)
sec_to_fir = distance[fir]
sec_to_n = distance[n]

result = min(start_to_fir + fir_to_sec + sec_to_n, start_to_sec + sec_to_fir + fir_to_n)

if int(1e9) <= result :
    print(-1)
else :
    print(result)