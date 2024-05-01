import sys

def count_ways_to_form_N(m, N):
    MOD = 10**9 + 7
    dp = [[0] * (N + 1) for _ in range(m + 1)]

    # Base case: when N is 0, there's only one way to form it (by not including any elements)
    for i in range(m + 1):
        dp[i][0] = 1

    for i in range(1, m + 1):
        for j in range(1, N + 1):
            # If N > 0, then for each i from 1 to m:
            if j >= arr[i - 1]:
                # Include the i-th element in forming N by recursively calling the function with N-i and i+1
                dp[i][j] = (dp[i-1][j-arr[i-1]] + dp[i][j]) % MOD
            else:
                # Don't include the i-th element, effectively skipping it. In this case, pass down the problem with N unchanged
                dp[i][j] = dp[i-1][j]
    return dp[m][N]

# Read input from stdin
m, N = map(int, input().split())
arr = list(map(int, input().split()))

print(count_ways_to_form_N(m, N))
