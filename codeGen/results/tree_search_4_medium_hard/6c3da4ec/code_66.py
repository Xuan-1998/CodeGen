def maximum_bitwise_or(n):
    s = input()
    n = int(n)
    dp = [0] * (n + 1)
    start = end = max_val = 0
    
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            start = end = i
            while end < n and s[end] == '1':
                end += 1
            dp[i] = max(2 ** (end - start) + dp[end], dp[start])
        else:
            end = i - 1
        max_val = max(max_val, dp[i])
    
    return bin(max_val)[2:]
