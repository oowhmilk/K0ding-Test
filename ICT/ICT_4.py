#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'closestColor' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY pixels as parameter.
#

def closestColor(pixels):
    # Write your code here
    colors = {
        "Black": (0, 0, 0),
        "White": (255, 255, 255),
        "Red": (255, 0, 0),
        "Green": (0, 255, 0),
        "Blue": (0, 0, 255)
    }
    
    result = []
    
    for pixel in pixels:

        red, green, blue = int(pixel[0:8], 2), int(pixel[8:16], 2), int(pixel[16:24], 2)
        
        min = pow(2, 31) - 1
        answer = ""
        
        for color, (check_red, check_green, check_blue) in colors.items():
            
            distance = ((red - check_red) ** 2 + (green - check_green) ** 2 + (blue - check_blue) ** 2)
            
            if distance < min:
                min = distance
                answer = color
            elif distance == min:
                answer = "Ambiguous"
        
        result.append(answer)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pixels_count = int(input().strip())

    pixels = []

    for _ in range(pixels_count):
        pixels_item = input()
        pixels.append(pixels_item)

    result = closestColor(pixels)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
