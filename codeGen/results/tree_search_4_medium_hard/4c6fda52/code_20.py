def min_changes(s, k):
    n = len(s)
    dp = {0: 0}
    for i in range(1, n+1):
        if i < k:
            dp[i] = float('inf')
        else:
            if s[i-k:i] in ['RGB', 'BGR']:
                dp[i] = min(dp.get(i-1, float('inf')), 1)
            elif s[i-k:i] == s[i-2*k+1:i]:
                dp[i] = min(dp.get(i-k, float('inf')), 0)
            else:
                dp[i] = dp.get(i-1, float('inf')) + 1
    return dp[n]

q = int(input())
for _ in range(q):
    n, k = map(int, input().split())
    s = input()
    print(min_changes(s, k))
