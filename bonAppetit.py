import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    kval = bill[k]
    val = 0
    for i, item in enumerate(bill):
        if i != k:
            val += item
    tot = val // 2
    if (b > tot):
        print(b - tot)
    else:
        print('Bon Appetit')

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
