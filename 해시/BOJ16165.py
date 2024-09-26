import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))

dict = {}
for _ in range(n) :
    team_name = input().strip()

    team_num = int(input())

    for _ in range(team_num) :
        name = input().strip()
        dict[name] = team_name
        
sorted_dict = sorted(dict.items())

for _ in range(m) :
    ques = input().strip()
    style = int(input())

    if style == 0 :
        for key, value in sorted_dict :
            if ques == value :
                print(key)
                
    else :
        for key, value in sorted_dict :
            if ques == key :
                print(value)