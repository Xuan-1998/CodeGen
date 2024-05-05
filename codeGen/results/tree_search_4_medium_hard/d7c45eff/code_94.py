def min_string(n, k):
    s = input().strip()
    dp = [False] * (k + 1)

    for i in range(1, k + 1):
        if i == 1:
            dp[i] = True
        elif i == 2:
            dp[i] = dp[0] and (s[0] <= s[-1])
        else:
            dp[i] = dp[i-1] or (dp[i-2] and (s[i-1] == s[-1]))

    if k < n:
        result = s[:k]
    else:
        result = ""
        for i in range(k):
            if dp[k]:
                result += s[-1]
            else:
                result += s[i]
            if i < k - 1 and dp[k-1]:
                break

    return result
