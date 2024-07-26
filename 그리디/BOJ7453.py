import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []
c = []
d = []

for i in range(n) :
    w, x, y, z = map(int, input().split(' '))
    a.append(w)
    b.append(x)
    c.append(y)
    d.append(z)

count = {}
for i in range(n) :
    for j in range(n) :
        sum = a[i] + b[j]
        if sum in count :
            count[sum] += 1
        else :
            count[sum] = 1

result = 0
for i in range(n) :
    for j in range(n) :
        sum = c[i] + d[j]
        if -sum in count :
            result += count[-sum]

print(result)
