import sys
input = sys.stdin.readline

def cal(a_list, b_list) :
    a_sum = 0
    b_sum = 0
    for i in range(len(a_list)) :
        for j in range(len(a_list)) :
            a_sum += arr[a_list[i]][a_list[j]]
            b_sum += arr[b_list[i]][b_list[j]]

    return abs(a_sum - b_sum)


def dfs(count, a_list, b_list) :
    global result
    if count == n :
        if len(a_list) == len(b_list) == m :
            dif = cal(a_list, b_list)
            result = min(result, dif)
        return
    
    dfs(count + 1, a_list + [count], b_list)
    dfs(count + 1, a_list, b_list + [count])

n = int(input())
m = int(n // 2)

arr = []
for _ in range(n) :
    arr.append(list(map(int, input().split(' '))))

result = int(1e9)
dfs(0, [], [])

print(result)