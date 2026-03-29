def max_bitwise_or_value():
    n = int(input())
    s = input()
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            if i > 1 and s[i - 2] == '1':
                dp[i] = max(dp[i - 1], int(s[i - 1], 2) | int(s[:i - 1].ljust(i, '0'), 2))
            else:
                dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1]
    
    return bin(max(dp))[2:]

print(max_bitwise_or_value())
