import sys

def min_operations(n, x):
    # Initialize dp array with infinity for all values except 1 (base case)
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: one-digit numbers have no operations

    while x:
        last_digit = int(str(x)[-1])
        for i in range(n, -1, -1):
            if i >= len(str(x)) + 1 and dp[i - len(str(x))]:
                dp[i] = min(dp[i], dp[i - len(str(x))] + 1)
        x //= 10
        n -= 1

    return -1 if dp[n] == float('inf') else dp[n]

# Read input from standard input
n, x = map(int, input().split())

print(min_operations(n, x))
