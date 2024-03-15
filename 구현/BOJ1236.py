import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))


arr = []
for i in range(n) :
    arr.append(input())

row = [0] * n
column = [0] * m

for i in range(n):
    for j in range(len(arr[i])) :
        if arr[i][j] == 'X' :
            if row[i] == 0 :
                row[i] = 1
            if column[j] == 0 :
                column[j] = 1

row_result = 0
for x in row :
    if x == 0 :
        row_result += 1

column_result = 0
for x in column :
    if x == 0 :
        column_result += 1

result = max(row_result, column_result)

print(result)
