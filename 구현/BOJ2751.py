import sys
input = sys.stdin.readline

def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            arr[k] = left[i]
            i += 1

        else :
            arr[k] = right[j]
            j += 1
        
        k += 1

    if i == len(left) :
        while j < len(right) :
            arr[k] = right[j] 
            j += 1
            k += 1

    elif j == len(right) :
        while i < len(left) :
            arr[k] = left[i]
            i += 1
            k += 1
    return arr


n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array)

for data in array:
    print(data)

