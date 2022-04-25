def staircase(n):
    # Write your code here
    i = 1
    sp = n - 2
    while i <= n:
        if sp >= 0:
            print(' ' * sp, '#' * i)
        else:
            print('#' * i)
        i += 1
        sp -= 1


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
