def find_digit_ones(n):
    MOD = 10**9 + 7
    dp = [0] * (n.bit_length() + 1)
    
    for i in range(1, n.bit_length() + 1):
        dp[i] = dp[i - 1] + ((1 << (i - 1)) // 2) % MOD
    
    total_count = 0
    for i in range(n.bit_length(), -1, -1):
        if (n >> i) & 1:
            total_count += dp[i]
    
    return total_count


# Receive input from stdin and print the answer to stdout.
n = int(input())
print(find_digit_ones(n))
