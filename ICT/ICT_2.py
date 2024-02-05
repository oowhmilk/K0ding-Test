#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countBetween' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY low
#  3. INTEGER_ARRAY high
#


def search(arr, target, find_left):
    left, right = 0, len(arr) - 1
    index = -1  

    while left <= right:
        mid = (left + right) // 2
        if find_left: 
            if arr[mid] >= target:
                index = mid
                right = mid - 1
            else:
                left = mid + 1
        else:  
            if arr[mid] <= target:
                index = mid
                left = mid + 1
            else:
                right = mid - 1

    return index

def countBetween(arr, low, high):
    results = []
    arr.sort() 
    
    for i in range(len(low)):

        left_index = search(arr, low[i], True)
        right_index = search(arr, high[i], False)
        
        if left_index == -1 or right_index == -1:
            count = 0
        else:
            if right_index >= left_index:
                count = right_index - left_index + 1
            else:
                count = 0
        results.append(count)
    
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    low_count = int(input().strip())

    low = []

    for _ in range(low_count):
        low_item = int(input().strip())
        low.append(low_item)

    high_count = int(input().strip())

    high = []

    for _ in range(high_count):
        high_item = int(input().strip())
        high.append(high_item)

    result = countBetween(arr, low, high)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
