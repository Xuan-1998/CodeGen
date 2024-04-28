def form_sums(N):
    m, arr = map(int, input().split())
    dp = {0: 1}
    max_val = max(arr)
    
    for i in range(1, N + 1):
        if i >= max_val:
            dp[i] = sum(dp.get(j, 0) for j in range(i))
        else:
            dp[i] = dp[i - max_val] + len([j for j in range(max_val + 1, i) if j % max_val == 0])
    
    return dp[N] % (10**9 + 7)

print(form_sums(int(input())))
