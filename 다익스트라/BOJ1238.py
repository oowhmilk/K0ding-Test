import heapq
import sys
input = sys.stdin.readline

def djikstra(start) :
    heap = []
    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap :
        dist, now = heapq.heappop(heap)

        if distance[now] < dist :
            continue
        
        for i in arr[now] :
            cost = dist + i[1]

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

n, m, x = map(int, input().split(' '))

arr = [[] for _ in range(n + 1)]
for _ in range(m) :
    a, b, c = map(int, input().split(' '))
    arr[a].append((b, c))

go = [0] * (n + 1)
for i in range(1, n + 1) :
    distance = [int(1e9)] * (n + 1)
    djikstra(i)
    go[i] = distance[x]

distance = [int(1e9)] * (n + 1)
djikstra(x)

max_size = 0
for i in range(1, n + 1) :
    max_size = max(max_size, go[i] + distance[i])

print(max_size)