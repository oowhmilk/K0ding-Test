import sys
input = sys.stdin.readline

s, e, q = input().strip().split(' ')
start = int(s[:2] + s[3:])
end = int(e[:2] + e[3:])
quit = int(q[:2] + q[3:])

dic = dict()
count = 0

while True :
    try :
        time, name = input().strip().split(' ')
        time = int(time[:2] + time[3:])

        if time <= start :
            dic[name] = 1
        elif end <= time <= quit :
            if name in dic and dic[name] == 1:
                count += 1
                dic[name] = 0
    except :
        break

print(count)