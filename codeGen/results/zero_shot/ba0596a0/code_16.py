import sys

def can_frog_cross(stones):
    n = len(stones)
    dp = [False] * (n + 1)

    # Base case: the frog can always reach the first stone
    dp[0] = True

    for i in range(1, n + 1):
        if dp[i - 1]:
            # If the previous jump is possible, check all three options
            for k in range(max(0, stones[i] - 2), stones[i]):
                dp[i] = (dp[i] or (k - 1) <= stones[i - 1] and dp[i - 1])
                if dp[i]:
                    break

    return dp[-1]

# Read input from stdin
stones = [int(x) for x in sys.stdin.readline().split()]

# Print the answer to stdout
print(can_frog_cross(stones))
