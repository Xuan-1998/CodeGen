def min_cuts(s):
    n = len(s)
    dp = [False] * (n + 1)

    for i in range(n):
        for j in range(i, -1, -1):
            if s[j:i+1] == s[i:j-1:-1]:
                dp[i] = True
                break

    return sum(1 for d in dp[1:] if not d)
