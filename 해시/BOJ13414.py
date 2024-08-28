import sys
input = sys.stdin.readline

k, l = map(int, input().split(' '))

dict = {}
for i in range(l) :
    num = input().strip()
    dict[num] = i

sorted_dict = sorted(dict.items(), key = lambda x : x[1])

if len(sorted_dict) < k :
    for i in range(len(sorted_dict)) :
        key, value = sorted_dict[i]
        print(key)
else :
    for i in range(k) :
        key, value = sorted_dict[i]
        print(key)