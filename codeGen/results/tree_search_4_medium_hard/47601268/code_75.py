def find_consecutive_ones(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        last_bit = (i & 1)  # 0 or 1
        if last_bit == 0:
            dp[i] = dp[i - 1]
        else:
            prev_bits = i >> 1  # previous bits
            if bin(prev_bits).count('1') >= 2:  # consecutive ones in previous bits
                dp[i] = dp[i - 1]
            else:
                dp[i] = 1 + dp[i - 1]
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(find_consecutive_ones(n))
