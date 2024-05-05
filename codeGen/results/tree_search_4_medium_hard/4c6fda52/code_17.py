def min_changes(s, k):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if s[i - 1] not in 'RGB':
            dp[i] = min(dp[i], dp[max(0, i - k)] + 1)
        else:
            dp[i] = dp[max(0, i - k)]

    return dp[-1]

while True:
    try:
        n, k = map(int, input().split())
        s = input()
        print(min_changes(s, k))
    except EOFError:
        break
