def count_binary(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        if not (i & 1):  # Last bit is 0
            dp[i] = dp[i - 1]
        elif i > 1 and not ((i >> 1) & 1):  # Last bit is 1, second-last bit is 0
            dp[i] = dp[i - 2] + dp[i // 2]
        else:
            dp[i] = 0

    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(count_binary(n))
