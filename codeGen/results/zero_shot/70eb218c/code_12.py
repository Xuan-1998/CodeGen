import sys

n = int(input())
x = int(input())

if x < 10**(n-1):
    ops = n - len(str(x))
else:
    for y in range(9, 0, -1):
        if str(x//y).zfill(n) == '0' * n + str(x//y)[1:]:
            ops = len(str(x)) - n
            break
    else:
        ops = -1

print(ops)
