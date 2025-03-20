import sys
input = sys.stdin.readline

arr = []
n, d, k, c = map(int, input().split(' '))

arr = [int(input()) for _ in range(n)]

window = arr[ : k]

result = 0
for i in range(n) :

  window.pop(0)
  window.append(arr[(i + k) % n])

  result = max(result, len(set(window + [c])))

  if result == d :
    break

print(result)