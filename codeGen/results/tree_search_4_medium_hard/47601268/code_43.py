def solve():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if not bin(i).count('1') % 2:  # Check if the number of ones is even
            dp[i] = dp[i - 1] + 1
    print(dp[n])
