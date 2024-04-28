def count_ways(m, N):
    MOD = 10**9 + 7
    
    # Initialize a dictionary to store memoized values
    dp = {0: 1}
    
    for i in range(1, m+1):
        total = 0
        for j in range(i, -1, -1):
            if N >= dp.get(j, 0):
                total += (N // (j + dp.get((i-1), 0)) % MOD)
        dp[i] = total % MOD
    
    return dp[m]

# Read input from standard input
m, N = map(int, input().split())

print(count_ways(m, N))
