arr = list(map(int, input().split(' ')))

sorted_arr = sorted(arr)

ascend = False
descend = False

for i in range(len(arr)) :
    if arr[i] == sorted_arr[i] :
        ascend = True
    else :
        ascend = False
        break

for i in range(len(arr)) :
    if arr[7 - i]  == sorted_arr[i] :
        descend = True
    else : 
        descend = False
        break

if ascend == True :
    print("ascending")
elif descend == True :
    print("descending")
else :
    print("mixed")



## 풀이 
arr = list(map(int, input().split(' ')))

ascend = True
descend = True

for i in range(1, 8) :
    if arr[i - 1] < arr[i] :
        descend = False
    elif arr[i - 1] > arr[i] :
        ascend = False

if ascend == True :
    print("ascending")
elif descend == True :
    print("descending")
else :
    print("mixed")