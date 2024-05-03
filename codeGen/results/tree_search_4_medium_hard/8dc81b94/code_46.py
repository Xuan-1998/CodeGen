def can_make_all_zero():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[False] * (max(a) + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for k in range(max(1, a[i - 1]), a[i - 1] - 1, -1):
            if dp[i - 1][k - 1]:
                dp[i][k] = True
    
    for k in range(len(dp[0])):
        if dp[n][k]:
            return "YES"
    return "NO"

print(can_make_all_zero())
