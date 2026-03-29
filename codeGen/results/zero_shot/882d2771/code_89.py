import sys

def f(n):
    return n

def calculate_expression(t, l, r):
    # Precalculate and store values of f(n) for all n from l to r
    fs = [0] * (r - l + 1)
    for i in range(l, r + 1):
        fs[i - l] = f(i)

    # Calculate the expression
    result = 0
    for ti, fi in zip(t, fs):
        result += ti * fi

    # Subtract l·f(r) and take the result modulo 10^9 + 7
    result -= l * fs[-1]
    return result % (10**9 + 7)

# Read input from stdin
t, l, r = map(int, sys.stdin.readline().split())

# Calculate and print the result to stdout
print(calculate_expression(t, l, r))
