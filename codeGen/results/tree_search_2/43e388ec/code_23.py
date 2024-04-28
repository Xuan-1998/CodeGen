import sys

# Read input from stdin
a = int(input())
b = int(input())

# Define the memoization table with zeros
dp = [[0] * (314160) for _ in range((1 << 20) + 1)]

def solve(a, b):
    # Base case: when any bit in a or b becomes zero
    if not a or not b:
        return 0

    # Initialize the state
    state = a & b

    # Perform dynamic programming and memoization
    res = dp[state][b]
    if res == 0:
        res = (1 << 31) - 1
    for i in range(10):
        if not (state >> i) & 1:
            break
        if state & ((1 << i) - 1):
            res ^= (1 << (i + b))
    dp[state][b] = res

    return res % (10**9 + 7)

print(solve(a, b))
