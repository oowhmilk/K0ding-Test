import sys
input = sys.stdin.readline

k, n = map(int, input().split(' '))

line = []
for _ in range(k) :
    line.append(int(input()))

min_line = 0
max_line = max(line)

while min_line < max_line :
    mid_line = int((min_line + max_line) // 2)

    count = 0
    
    for x in line :
        count += x // mid_line

    if count >= n :
        min_line = mid_line + 1
    else : 
        max_line = mid_line - 1

print(max_line)