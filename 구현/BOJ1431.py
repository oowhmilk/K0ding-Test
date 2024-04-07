import sys
input = sys.stdin.readline

n = int(input())

result = []
for i in range(n) :
    data = input().strip()

    arr = []
    arr = list(data)

    length = len(arr)

    sum = 0
    for j in range(len(arr)) :
        if '0' <= arr[j] <= '9' :
            sum += int(arr[j])

    result.append((length, sum, data))

# result = sorted(result, key = lambda x : x[1])
result = sorted(result)

for i in result :
    print(i[2])