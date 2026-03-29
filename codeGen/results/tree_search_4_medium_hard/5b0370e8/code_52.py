import sys

# Read input from stdin
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # Initialize the DP table
    dp = [[0] * (1 << k) for _ in range(k + 1)]
    
    # Base case: one way to get an empty array with bitwise AND result 0
    dp[0][0] = 1
    
    for i in range(1, k + 1):
        for mask in range(1 << k):
            # If the current element is less than $2^k$, update dp[i][mask]
            if (arr[i - 1] & mask) < (1 << k):
                dp[i][mask] = (dp[i - 1][arr[i - 1] & mask] + dp[i - 1][mask]) % (10**9 + 7)
            # If the current element is equal to $2^k-1$, consider two sub-cases
            elif arr[i - 1] == (1 << k) - 1:
                and_result = (1 << k) - 1
                for j in range(i):
                    if mask & (1 << j):
                        and_result &= (arr[j] & (1 << j))
                if and_result >= mask:
                    dp[i][mask] = dp[i - 1][and_result]
                else:
                    dp[i][mask] = dp[i - 1][mask]
    
    # Return the count modulo $10^9+7$
    print(sum(dp[k]) % (10**9 + 7))
