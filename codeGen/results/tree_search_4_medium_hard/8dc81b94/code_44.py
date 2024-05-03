def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [[False] * (max(arr) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for k in range(1, max(arr) + 1):
            if all(x <= k for x in arr[:i]):
                dp[i][k] = True
            else:
                break
    
    return "YES" if any(dp[-1]) else "NO"
