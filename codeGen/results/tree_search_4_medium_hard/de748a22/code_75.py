def minSignVariableSumRemoval(n, q, signs):
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Calculate sign-variable sum for each prefix of the array.
    s_sum = [0]
    for i in range(1, n + 1):
        if signs[i - 1] == '+':
            s_sum.append(s_sum[-1] + 1)
        else:
            s_sum.append(s_sum[-1] - 1)

    # Fill up the dynamic programming table.
    for i in range(n, -1, -1):
        for j in range(i + 1, n + 1):
            if signs[i] == '+' and signs[j - 1] == '-':
                dp[i][j] = True
            elif s_sum[j] - s_sum[i] % 2 == 0:
                dp[i][j] = (dp[i][i + 1] or sum(signs[i + 1:i + k]) % 2 != 0 for k in range(1, j - i))[0]

    # Process the queries.
    res = []
    for _ in range(q):
        l, r = map(int, input().split())
        res.append(sum(dp[l][r] for _ in range(r - l + 1)))
    
    print(*res)
