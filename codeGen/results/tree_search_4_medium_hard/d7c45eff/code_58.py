def smallest_string(k, s):
    dp = ["" for _ in range(k+1)]
    dp[0] = ""
    
    for i in range(1, k+1):
        if i >= len(s):
            dp[i] = dp[i-1]
        elif s[i-1] < dp[i-1]:
            dp[i] = s[i-1] + dp[i-1]
        else:
            dp[i] = dp[i-1]

    return dp[k]

k, n = map(int, input().split())
s = input()
print(smallest_string(k, s))
