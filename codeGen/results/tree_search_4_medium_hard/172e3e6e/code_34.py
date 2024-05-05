def good_subsequences():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize dp table with base cases
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        if a[i - 1] == 1:
            dp[i][1] = True
    
    # Iterate over each possible length of the subsequence
    for i in range(2, n + 1):
        # For each possible largest divisor from 2 to max element in a
        for last_divisor in range(2, max(a) + 1):
            if a[i - 1] % last_divisor == 0:
                dp[i][last_divisor] = (dp[i - 1][last_divisor] or 
                                        (a[i - 1] // last_divisor > 0 and dp[i - 1][a[i - 1] // last_divisor]))
    
    # Return the total count of states where last_divisor > 1, as these represent good subsequences
    return sum(1 for i in range(2, n + 1) if dp[n][i])
