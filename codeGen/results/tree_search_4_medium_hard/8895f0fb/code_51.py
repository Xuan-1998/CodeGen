def expected_carries(N):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i):
            k = i - j
            if j == 0 or k == 0:
                dp[i] += dp[j-1] * dp[k-1]
            else:
                dp[i] += dp[j-1] * dp[k-1] + (j >= 1 and k >= 1) / (i+1)
        dp[i] /= (2*i)
    return dp[N]

T = int(input())
for _ in range(T):
    N = int(input())
    print(expected_carries(N))
