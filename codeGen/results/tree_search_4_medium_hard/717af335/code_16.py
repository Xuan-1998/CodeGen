import sys

def find_x_and_y():
    A = int(input())
    B = int(input())

    for X in range(0, (A + B) // 2 + 1):
        Y = A - X
        if B == X ^ Y:
            return "{} {}".format(X, Y)

    return "-1"

print(find_x_and_y())
