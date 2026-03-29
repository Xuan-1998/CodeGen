import sys
from math import factorial

T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())

    # A 2x2 matrix with trace N has the form:
    # | a + b, c |
    # | a + c, -a-b |
    # where a + b + c = N.
    for a in range(N // 3 + 1):
        b = (N - 2 * a) // 2
        if b >= 0 and (a > 0 or b > 0):
            det = a * (a - b)
            if det > 0:
                print(1)  # The number of such matrices is 1.
                break
    else:
        print(0)  # There are no such matrices.
