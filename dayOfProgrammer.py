import os


def dayOfProgrammer(year_value):
    test = 256
    monthdays = [31, 0, 31, 30, 31, 30, 31, 31, 31, 31, 30, 31]
    i = 0

    if year_value > 1917:
        if year_value == 1918:
            monthdays[1] = 29
            while test >= 28:
                test -= monthdays[i]
                i += 1
            dd = 26
            mm = i + 1
            if mm < 10:
                mm = str(0) + str(mm)
        else:
            if year_value % 400 == 0 or ((year_value % 4 == 0) and not (year_value % 100 == 0)):
                # If it a leap
                monthdays[1] = 29
                while test >= 28:
                    test -= monthdays[i]
                    i += 1
                dd = test
                mm = i + 1
                if (mm < 10):
                    mm = str(0) + str(mm)
            else:
                monthdays[1] = 28
                # If not a leap year
                while test > 28:
                    test -= monthdays[i]
                    i += 1
                dd = test
                mm = i + 1
                if mm < 10:
                    mm = str(0) + str(mm)
    else:
        if year_value % 4 == 0:
            # If it a leap
            monthdays[1] = 29
            while test >= 28:
                test -= monthdays[i]
                i += 1
            dd = test
            mm = i + 1
            if mm < 10:
                mm = str(0) + str(mm)
        else:
            monthdays[1] = 28
            # If not a leap year
            while test > 28:
                test -= monthdays[i]
                i += 1
            dd = test
            mm = i + 1
            if mm < 10:
                mm = str(0) + str(mm)
    yyyy = str(dd) + '.' + str(mm) + '.' + str(year_value)
    return yyyy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
