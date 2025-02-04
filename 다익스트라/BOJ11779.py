import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, end) :
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap :
        dist, now = heapq.heappop(heap)
        if now == end :
            break
        if dist < distance[now] :
            continue
        for i in arr[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                prev[i[0]] = now
                heapq.heappush(heap, (cost, i[0]))

n = int(input())

arr = [[] for _ in range(n + 1)]
for _ in range(int(input())) :
    a, b, c = map(int, input().split(' '))
    arr[a].append((b, c))

start, end = map(int, input().split(' '))

distance = [int(1e9)] * (n + 1)
prev = [0] * (n + 1)
dijkstra(start, end)

print(distance[end])

path = [end]
now = end
while now != start:
    now = prev[now]
    path.append(now)

path.reverse()
print(len(path))
for x in path :
    print(x, end = ' ')