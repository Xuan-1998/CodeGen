from math import ceil

def solve(n, t):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = ceil(dp[i - 1] / 10) if i > 0 else 1
    return min(dp[n], t)

# Read input from stdin
n, t = map(int, input().split())
frac = [int(x) for x in input().split('.')]

# Main function to solve the problem
print(solve(n, t))
