def min_cuts(s):
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i):
            if s[j:i].lower() == s[j:i].lower()[::-1]:
                dp[i] = min(dp[i], dp[j - 1] + 1)
        dp[i] = max(dp[i], 0)

    return dp[-1]

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
