def solve():
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    max_Arr = max(Arr)
    
    dp = [[0] * (max_Arr + 1) for _ in range(N+1)]
    
    for i in range(1, N+1):
        max_val = max(Arr[:i])
        if max_val > K:
            dp[i][max_val] += 1
        for j in range(max_val, -1, -1):
            if Arr[i-1] > j and dp[i-1][j]:
                dp[i][j] += dp[i-1][j]
    
    ans = sum([dp[N][i] for i in range(K+1, max_Arr + 1)])
    print(ans)
