import sys
input = sys.stdin.readline

def combination(n, new_arr, count) :
    global answer

    if len(new_arr) == n :
        result = cal(new_arr)
        answer = min(answer, result)
    
    for i in range(count, len(chicken)) :
        combination(n, new_arr + [chicken[i]], i + 1)

def cal(new_arr) :
    
    result = 0

    for home_x, home_y in home :
        
        dist = int(1e9)
        for chicken_x, chicken_y in new_arr :
            dist = min(dist, abs(chicken_x - home_x) + abs(chicken_y - home_y))

        result += dist

    return result

n, m = map(int, input().split(' '))

arr = []
home = []
chicken = []
answer = int(1e9)

for i in range(n) :
    check = list(map(int, input().split(' ')))

    for j in range(n) :
        if check[j] == 1 :
            home.append((i, j))
        if check[j] == 2 :
            chicken.append((i, j))

combination(m, [], 0)

print(answer)