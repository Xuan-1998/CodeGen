def count_blocks(n):
    MOD = 998244353
    dp = [0] * (n + 1)
    
    # Initialize dp[0] to 1, since there is only one block of length 0
    dp[0] = 1
    
    for i in range(1, n + 1):
        same_last_digit = False
        if i >= n:
            same_last_digit = True
        
        # Calculate the number of blocks ending at position i with lengths from 1 to n
        for k in range(1, min(i + 1, n) + 1):
            if not same_last_digit and k == 1:
                dp[i] += 1
            elif same_last_digit and k < i - n + 2:
                dp[i] += dp[i - n]
        
        # Update the number of blocks ending at position i with length 1
        dp[i] = (dp[i] + MOD) % MOD
    
    return ' '.join(str(x) for x in dp[1:])
