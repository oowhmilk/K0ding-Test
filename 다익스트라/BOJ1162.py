import heapq
import sys
input = sys.stdin.readline

def dijkstra(start) :
    heap = []
    heapq.heappush(heap, (0, start, 0))
    distance[start][0] = 0

    while heap :
        dist, now, count = heapq.heappop(heap)

        if distance[now][count] < dist :
            continue

        for i in arr[now] :
            cost = dist + i[1]
            if cost < distance[i[0]][count] :
                distance[i[0]][count] = cost
                heapq.heappush(heap, (cost, i[0], count))
            
            if count < k and dist < distance[i[0]][count + 1] :
                distance[i[0]][count + 1] = dist
                heapq.heappush(heap, (dist, i[0], count + 1))


n, m, k = map(int, input().split(' '))

arr = [[] for _ in range(n + 1)]
for _ in range(m) :
    a, b, c = map(int, input().split(' '))
    arr[a].append((b, c))
    arr[b].append((a, c))

distance = [[int(1e17)] * (k + 1) for _ in range(n + 1)]
dijkstra(1)

result = int(1e17)
for i in range(k + 1) :
    result = min(result, distance[n][i])

print(result)