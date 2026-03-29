def count_numbers(n):
    # Initialize dp array
    dp = [0] * (n + 1)
    
    # Base case: there is only one way to represent a number with no consecutive ones in its binary representation - that's the number itself
    for i in range(2**n):
        if str(bin(i))[2:].count('1') == 1:
            dp[i] = 1
    
    # Fill up the dp array using dynamic programming
    for i in range(n + 1):
        if i > 0:
            for j in range(2**i):
                if str(bin(j))[2:].count('1') == 1 and not any(str(bin(k))[2:]).find('11' for k in range(j, 2**i)):
                    dp[i] += 1
    
    return dp[n]
