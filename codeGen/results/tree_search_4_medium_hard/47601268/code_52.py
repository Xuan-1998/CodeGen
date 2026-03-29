def no_consecutive_ones(n):
    dp = [False] * (n + 1)
    for i in range(2, n + 1):
        if bin(i)[2:].count('1') > 0 and all(int(b) != int(a) or b == '0' for a, b in zip(bin(i - 1)[2:], bin(i)[2:])):
            dp[i] = True
    return sum(1 for i in range(n + 1) if dp[i])
