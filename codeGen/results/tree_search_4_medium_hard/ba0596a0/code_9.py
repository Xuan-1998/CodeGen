from sys import stdin

def can_cross_stones(stones):
    n = len(stones)
    dp = [[False] * 3 for _ in range(n+1)]

    # Base case: start from scratch (0th stone)
    dp[0][0], dp[0][1], dp[0][2] = True, True, True

    for i in range(1, n):
        for j in {0, 1, 2}:
            if not dp[i-1][j]:
                continue
            k = stones[i] - stones[i-1]
            if abs(k-j) > 1:
                dp[i][j] = False
                continue

            # Check if the frog can reach this stone with a jump of j units and previous jump was k
            if j == k+1 or (k >= 0 and j == k+1):
                dp[i][j] = True
            elif j == k-1:
                dp[i][j] = False

    return dp[-1][-1]

# Read input from stdin
stones = list(map(int, stdin.readline().strip().split()))

# Print the result to stdout
print(can_cross_stones(stones))
