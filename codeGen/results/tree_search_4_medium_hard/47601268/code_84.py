def count_binary_strings(n):
    dp = [[0] * (n + 1) for _ in range(20)]
    
    # Base case: all binary strings with k consecutive ones are of the form 11...110
    for i in range(2**k, n+1):
        if bin(i).count('1') < 2:
            dp[0][i] = 1
    
    for k in range(1, 20):
        for i in range(2**k, n+1):
            if bin(i).count('1') < 2:
                dp[k][i] = dp[k-1][i//2] + dp[0][i]
    
    return sum(dp[-1])

n = int(input())
print(count_binary_strings(n))
