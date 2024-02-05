#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxTrailing' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxTrailing(arr):
    # Write your code here
    diff = -1
    value = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > value:
            diff = max(diff, arr[i] - value)
        else:
            value = arr[i]
    
    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxTrailing(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
