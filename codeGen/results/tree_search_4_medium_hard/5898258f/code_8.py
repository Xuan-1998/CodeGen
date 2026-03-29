def solve():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if i % 2 == 0:
            dp[i] = max(dp[i - 1], dp[(i // 2) - 1] ^ A[i - 1])
        else:
            dp[i] = max(dp[i - 1], A[i - 1] ^ X)
    
    print(max(dp))
