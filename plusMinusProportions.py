#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    propPos = 0
    propNeg = 0
    propZero = 0

    for num in arr:
        if (num < 0):
            propNeg += 1
        elif (num > 0):
            propPos += 1
        else:
            propZero += 1

    total = propPos + propNeg + propZero
    print("{:.6f}".format(propPos / total))
    print("{:.6f}".format(propNeg / total))
    print("{:.6f}".format(propZero / total))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
