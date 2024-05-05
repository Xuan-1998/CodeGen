import sys

def min_operations(n, x):
    if n == 1:
        return 0
    str_x = str(x)
    while len(str_x) < n:
        new_x = ''
        for digit in str_x:
            new_x += str(int(digit) * int(digit))
        str_x = str(new_x)
    if len(str_x) > n:
        return -1
    return len(str_x) - 1

n, x = map(int, input().split())
print(min_operations(n, x))
