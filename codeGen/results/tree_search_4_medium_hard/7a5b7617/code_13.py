import sys

def solve(N, M):
    dp = {i: {} for i in range(N+1)}
    
    for n_rows in range(1, N+1):
        for last_sum in range(M+1):
            if n_rows == 1:
                dp[n_rows][last_sum] = 1
            else:
                total_ways = 0
                for k in range(last_sum + 1):
                    total_ways += min(k, M) * (dp.get(n_rows-1, {}).get(max(0, k-1), 0))
                dp[n_rows][last_sum] = total_ways % (10**9 + 7)
    
    return dp[N][0]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))
