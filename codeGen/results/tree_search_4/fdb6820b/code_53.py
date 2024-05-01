from collections import defaultdict

def solve(m, N, arr):
    total_sum = sum(arr)
    if total_sum <= N:
        MOD = 10**9 + 7
        dp = [defaultdict(int) for _ in range(N+1)]
        dp[0][0] = 1
        
        for x in arr:
            for i in range(min(x, N), -1, -1):
                for j in range(len(dp[i])):
                    dp[i+x][j] += dp[i][j]
                    if (i+x) % MOD == 0 and i > 0:
                        break
            if total_sum <= N:
                return sum(dp[N].values()) % MOD
        return 1
    else:
        return 0

m, N = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(m, N, arr))
