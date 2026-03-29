def min_F(n, s, seq):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if i % 2 == 1:
            for j in range(i // 2 + 1):
                dp[i] = min(dp[i], dp[j] + seq[j] * (seq[i - 1] - s))
        else:
            for j in range((i - 1) // 2 + 1):
                dp[i] = min(dp[i], dp[j] + (seq[i - 1] - s))

    return dp[n]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    seq = list(map(int, input().split()))
    print(min_F(n, s, seq))
