import sys
input = sys.stdin.readline

n, s= map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

left = 0
right = 1

total = arr[left] + arr[right]
min_size = int(1e9)

for x in arr :
    if s <= x :
        print(1)
        sys.exit()


while right != n - 1 :
     
    if total < s:
        right += 1
        total += arr[right]
    else :
        min_size = min(min_size, right - left + 1)
        if left + 1 == right :
            total -= arr[left]
            left += 1
            right += 1
            total += arr[right]
        else :
            total -= arr[left]
            left += 1


if left == 0 and right == n - 1 :
    if total < s :
        print(0)
        sys.exit()

while left != n - 1 :
     
    if total >= s:
        min_size = min(min_size, right - left + 1)
        total -= arr[left]
        left += 1
    else :
        break

print(min_size)