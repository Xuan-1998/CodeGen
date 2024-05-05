def minChanges(s, k):
    n = len(s)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    
    expected_color = 'R' if s[-(k-1)] == 'G' else 'G' if s[-(k-1)] == 'B' else 'B'
    
    for i in range(k - 1, n):
        dp[i][k] = min(dp[max(i-k+1, 0)][j-1] + (s[i-k+1] != expected_color) for j in range(min(i-k+2, k), k+1))
        
    return dp[n-1][k]

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    s = input().strip()
    
    print(minChanges(s, k))

