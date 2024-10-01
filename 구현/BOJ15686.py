import sys
input = sys.stdin.readline

def combinations(n, new_arr, c) :
    global chick
    global result

    if len(new_arr) == n :
        
        total_value = 0
        for j in range(len(house)) :

            min_value = int(1e9)
            for k in range(len(new_arr)) :
                x1, y1 = house[j]
                x2, y2 = new_arr[k]
                min_value = min(min_value, abs(x1 - x2) + abs(y1 - y2))
                
            total_value += min_value

        result = min(total_value, result)
    
    for i in range(c, len(chick)) :
        combinations(n, new_arr + [chick[i]], i + 1)


n, m = map(int, input().split(' '))

house = []
chick = []

result = int(1e9)

for i in range(n) :
    check = list(map(int, input().split(' ')))

    for j in range(len(check)) :
        if check[j] == 1 : 
            house.append((i, j))
        elif check[j] == 2 :
            chick.append((i, j))

combinations(m, [], 0)

print(result)