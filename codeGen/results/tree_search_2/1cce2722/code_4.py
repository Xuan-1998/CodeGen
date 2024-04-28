def solve():
    n = int(input())
    sequence = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    for s in range(2, n + 1):
        if sequence[s - 1] == s:
            dp[s] = max(dp[max(0, s - 2)] + s if s >= 2 else 0, 
                        dp[max(0, s - 1)] + 1 if s > 0 else 0)
        else:
            dp[s] = dp[s - 1]
    
    print(max(dp))
