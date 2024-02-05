#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countMatches' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid1
#  2. STRING_ARRAY grid2
#

def dfs(grid, x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid) or grid[x][y] == '0' or visited[x][y]:
        return []
    
    visited[x][y] = True
    area = [(x, y)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4) :

        new_x = x + dx[i]
        new_y = y + dy[i]

        new_area = dfs(grid, new_x, new_y, visited)

        for check in new_area:
            if check not in area:
                area.append(check)

    return area

def find_areas(grid):
    visited = [[False for _ in range(len(grid))] for _ in range(len(grid))]
    areas = []

    for i in range(len(grid)):

        for j in range(len(grid)):

            if grid[i][j] == '1' and not visited[i][j]:
                areas.append(dfs(grid, i, j, visited))

    return areas

def countMatches(grid1, grid2):
    areas1 = find_areas(grid1)
    areas2 = find_areas(grid2)

    matches = 0

    for area1 in areas1:

        if any(area1 == area2 for area2 in areas2):
            matches += 1

    return matches


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

grid1_count = int(input().strip())

grid1 = []

for _ in range(grid1_count):
    grid1_item = input()
    grid1.append(grid1_item)

grid2_count = int(input().strip())

grid2 = []

for _ in range(grid2_count):
    grid2_item = input()
    grid2.append(grid2_item)

result = countMatches(grid1, grid2)

print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
