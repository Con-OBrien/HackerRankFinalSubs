import os


def kangaroo(x1, v1, x2, v2):
    # create 2 seperate lists based on kangaroo positions, k1, k2
    # compare 2 lists for same value, if present check if index is the same
    k1 = [0] * 10000
    k2 = [0] * 10000
    i = 1
    prev = x1
    k1[0] = x1
    while i < 10000:
        k1[i] = v1 + prev
        prev += v1
        i += 1
    j = 1
    prev2 = x2
    k2[0] = x2
    while j < 10000:
        k2[j] = v2 + prev2
        prev2 += v2
        j += 1

    if any(z == y for z, y in zip(k1, k2)):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
