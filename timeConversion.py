import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    newTime = ''
    h = s[0:2]
    m = s[3:5]
    sec = s[6:8]
    ampm = s[8:11]

    if (ampm == 'PM'):
        if (h == '12'):
            newTime += h + ':' + m + ':' + sec
        else:
            newTime = str((int(h) + 12))
            newTime += ':' + m + ':' + sec
    if (ampm == 'AM'):
        if (h == '12'):
            h = str(int(h) - 12)
            newTime += h + '0' + ':' + m + ':' + sec
        else:
            newTime += h + ':' + m + ':' + sec

    return newTime


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
