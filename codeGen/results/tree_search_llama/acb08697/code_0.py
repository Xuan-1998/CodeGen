import sys

def min_stones(n, ops):
    x = 0  # initial number of stones
    for op in ops:
        if op == '-':  # remove stone
            x -= 1
        else:  # add stone
            x += 1
        x = max(x, 0)  # ensure non-negative
    return x

n = int(sys.stdin.readline())
ops = sys.stdin.readline().strip()
print(min_stones(n, ops))
