from collections import defaultdict
import sys

def solve(m, N, arr):
    MOD = 10**9 + 7
    
    dp = [0] * (N+1)
    dp[0] = 1
    
    freq_map = defaultdict(int)
    for num in arr:
        freq_map[num] += 1
    
    for i in range(1, N+1):
        if freq_map[i]:
            dp[i] = 1
        else:
            for j in range(i-1, -1, -1):
                dp[i] = (dp[i] + dp[j]) % MOD
    
    return dp[N]

m, N = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(m, N, arr))
