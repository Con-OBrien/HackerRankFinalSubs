#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    res = 0
    l2R = 0
    r2L = 0
    i = 0
    j = 0
    while i <= (len(arr) - 1):
        l2R += arr[i][j]
        i += 1
        j += 1
    i -= 1
    j = 0
    while i >= 0:
        r2L += arr[i][j]
        i -= 1
        j += 1
    res = abs(l2R - r2L)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
