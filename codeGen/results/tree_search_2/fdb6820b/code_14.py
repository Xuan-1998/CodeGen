def count_ways(m, N, arr):
    MOD = 10**9 + 7

    dp = [0] * (N + 1)
    dp[0] = 1  # base case: one way to form a sum of 0 is to not include any numbers

    for i in range(1, N + 1):
        for j in range(i):
            if arr[j] <= i:
                dp[i] += dp[j]
                dp[i] %= MOD

    return dp[N]

# Read input from stdin
m = int(input())
N = int(input())
arr = [int(x) for x in input().split()]

# Calculate and print the result
result = count_ways(m, N, arr)
print(result)
