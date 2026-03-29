import sys

# Read input from stdin
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

# Create a table to store the maximum total joy for each prefix of hares
dp = [0] * (n + 1)
for i in range(1, n + 1):
    # Transition function: consider three cases and update dp[i]
    if i == 1:
        dp[i] = max(a[0], c[0])
    elif i == 2:
        dp[i] = max(a[0] + b[1], a[1] + c[0])
    else:
        dp[i] = max(dp[i - 1] + a[i - 1],
                    dp[i - 2] + b[i - 1] if i % 2 == 0 else c[i - 2])

# Print the maximum total joy for all hares
print(dp[n])
