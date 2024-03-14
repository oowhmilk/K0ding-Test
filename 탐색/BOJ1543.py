string = input()
compare = input()
index = 0
result = 0
while len(string) - index >= len(compare):
    if string[index:index + len(compare)] == compare: 
        result += 1
        index += len(compare)
    else:
        index += 1
print(result)