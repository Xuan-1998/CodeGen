import sys

def min_function_value(n, s, a):
    # Initialize minimum value to infinity
    min_value = float('inf')

    for x in range(s + 1):
        y = s - x
        if (x * y >= 0):  # Check if both are positive or negative
            value = sum(x_i * y_i for x_i, y_i in zip(a[1:], a[:-1]))
            min_value = min(min_value, value)

    return min_value

t = int(sys.stdin.readline())
for _ in range(t):
    n, s = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(min_function_value(n, s, a))
