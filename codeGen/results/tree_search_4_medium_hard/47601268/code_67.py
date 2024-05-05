def no_consecutive_ones(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        count = sum(1 for k in range(i) if not any((k << 1) | 1 & pow(2, j) for j in range(i.bit_length())))
        dp[i] = count
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(no_consecutive_ones(n))
