import heapq
import sys
input = sys.stdin.readline

def dijkstra() :
    global interview

    heap = []
    for x in interview :
        heapq.heappush(heap, (0, x))
        distance[x] = 0

    while heap :
        dist, now = heapq.heappop(heap)

        if distance[now] < dist :
            continue

        for i in arr[now] :
            cost = dist + i[1]

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(heap,(cost, i[0]))


n, m, k = map(int, input().split(' '))

arr = [[] for _ in range(n + 1)]
for _ in range(m) :
    u, v, c = map(int, input().split(' '))
    arr[v].append((u, c))

interview = set(map(int, input().split(' ')))

max_value = 0
answer = -1

distance = [int(1e11)] * (n + 1)
dijkstra()
max_value = 0
answer = -1
for i in range(len(distance)) :
    if distance[i] != int(1e11) :
        if max_value != max(max_value, distance[i]) :
            max_value = max(max_value, distance[i])
            answer = i

print(answer)
print(max_value)
