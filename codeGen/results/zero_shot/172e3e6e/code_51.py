def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize dp table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: an empty subsequence is good
    dp[0][0] = 1
    
    # Iterate over the array and subsequence lengths
    for i in range(1, n + 1):
        for j in range(min(i, n) + 1):
            # If the current number is divisible by j
            if a[i - 1] % j == 0:
                # The subsequence ending with this number is good
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][j]) % (10**9 + 7)
            else:
                # The subsequence does not end with this number
                dp[i][j] = dp[i - 1][j]
    
    # Calculate the total number of good subsequences modulo 10^9 + 7
    result = sum(dp[n][i] for i in range(n, 0, -1))
    print(result % (10**9 + 7))

if __name__ == "__main__":
    solve()
