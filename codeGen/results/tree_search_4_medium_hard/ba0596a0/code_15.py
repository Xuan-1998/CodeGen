import sys

def can_cross_stones(stones):
    n = len(stones)
    dp = [False] * n
    dp[0] = True

    for i in range(1, n):
        for k in range(min(3, stones[i]-stones[i-1]), 2):
            if (stones[i] - stones[i-1]) % 3 == (k-1) % 3 and dp[i-1]:
                dp[i] = True
                break
        else:
            dp[i] = False

    return dp[-1]

# Read input from stdin
n = int(input())
stones = [int(x) for x in input().split()]

# Print the result to stdout
print(can_cross_stones(stones))
