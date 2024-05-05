def countOnes(n):
    dp = [0] * (n + 1)
    
    for i in range(9): # single-digit numbers
        if i == 1:
            dp[i] = n // 10 ** (i + 1) + n // 10 ** i
        elif i == 4: # and multiples of 11
            dp[i] = dp[i - 2]
        else:
            dp[i] = (n // 10 ** (i + 1)) * (10 ** i)
    
    for i in range(9, n.bit_length() + 1):
        if i == 0: # no single-digit numbers
            dp[n] += n
        else:
            dp[n] += (n // 10 ** i) * (10 ** (i - 1))
        
        for j in range(i - 1, 0, -1): # count multiples of 10^j and 11^j
            if j == 4: 
                break
            dp[n] += (n // 10 ** i) * (10 ** (i - 1))
    
    for i in range(n.bit_length() + 1):
        for j in range(9, n.bit_length()):
            dp[n] += ((n >> j) & 1)
            
    return dp[n]
