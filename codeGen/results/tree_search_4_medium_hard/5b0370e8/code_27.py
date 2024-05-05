def count_ways(n, k):
    MOD = 10**9 + 7
    dp = [[0] * (1 << k) for _ in range(k+1)]
    
    # Base case: when k = 0, there is only one way to form an array with no elements
    for i in range(2**k):
        dp[0][i] = 1
    
    # Fill up the table using dynamic programming
    for i in range(1, k+1):
        for j in range(1 << i):
            if j < (1 << (i-1)):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = 0
                for p in range(i-1):
                    if (j ^ (1 << p)) < (1 << i):
                        dp[i][j] += dp[p][(j ^ (1 << p))]
                        dp[i][j] %= MOD
    
    # Calculate the final answer by summing up the values in the last row of the table
    ans = 0
    for j in range(1 << k):
        ans += dp[k][j]
        ans %= MOD
    
    return ans

# Read input from standard input
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Count the number of arrays that satisfy the condition
    count = 0
    for i in range(1 << n):
        xor_sum = 0
        and_sum = 0
        for j in range(n):
            if (i >> j) & 1:
                xor_sum ^= a[j]
                and_sum &= a[j]
        if xor_sum >= and_sum:
            count += 1
    
    # Print the answer to standard output
    print(count % MOD)
