import sys
input = sys.stdin.readline

n = int(input())
dict = {}
arr = []

for i in range(n) :
    x = input()

    if x not in dict:
        dict[x] = 1
    elif x in dict :
        dict[x] += 1

target = max(dict.values())

for book, number in dict.items() :
    if number == target :
        arr.append(book)

print(sorted(arr)[0])