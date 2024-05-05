def smallest_string(n, k):
    s = input().strip()
    dp = {0: ""}
    
    for i in range(1, n+1):
        state = i - 1
        if state > len(dp):
            new_state = state + (k-i)
            dp[state] = min((dp.get(j) or s[:i]).ljust(k)[::-1] for j in range(state-1, -1, -1)), key=lambda x: x[::-1])
        else:
            dp[state] = dp[0].ljust(k)[:state]
    
    return dp[k-1].ljust(k)
