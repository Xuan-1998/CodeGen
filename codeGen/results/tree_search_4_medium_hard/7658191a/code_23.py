import sys

def max_score(n, k, z, arr):
    # Sort the array in descending order as per your idea
    arr.sort(reverse=True)

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base cases: when i=0 or j=0
    for j in range(k + 1):
        dp[0][j] = 0

    for i in range(1, n + 1):
        dp[i][0] = arr[i - 1]

    # Fill up the DP table using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j <= z:
                # Choose the maximum score: either move right or left
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i - 1])
            else:
                # No more than z moves to the left, so only move right
                dp[i][j] = dp[i - 1][j]

    return dp[n][k]

# Read input and print output
t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(n, k, z, arr))
