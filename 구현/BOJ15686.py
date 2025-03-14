import sys
input = sys.stdin.readline

def combinations(n, new_arr, c) :
    
    global result

    if len(new_arr) == n :
        total = 0
        for j in range(len(home)) :

            min_value = int(1e9)
            for k in range(len(new_arr)) :
                x1, y1 = home[j]
                x2, y2 = new_arr[k]

                min_value = min(min_value, abs(x1 - x2) + abs(y1 - y2))
            
            total += min_value

        result = min(total, result)

    
    for i in range(c, len(chicken)) :
        combinations(n, new_arr + [chicken[i]], i + 1)

n, m = map(int, input().split(' '))
arr = []

home = []
chicken = []
result = int(1e9)

for i in range(n) :
    check = list(map(int, input().split(' ')))

    for j in range(n) :
        if check[j] == 1 :
            home.append((i, j))
        elif check[j] == 2 :
            chicken.append((i, j))

combinations(m, [], 0)
print(result)