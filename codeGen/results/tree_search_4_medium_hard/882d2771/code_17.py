import sys

# Define a dictionary to store the results of subproblems
dp = {1: 0}

def f(n):
    if n not in dp:
        if n % 2 == 0:
            m = n // 2
            dp[n] = f(m) + 1
        else:
            dp[n] = min(f((n - 1) // 2), n - 1)
    return dp[n]

# Read the input from standard input
t, l, r = map(int, input().split())

# Calculate and print the result modulo 109+7
result = sum(t * f(i) for i in range(l, r+1)) % (10**9 + 7)
print(result)
