import sys
from collections import defaultdict

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [0] * (n + 1)
    for i in range(1, min(n+1, m)+1):
        dp[i] = sum((s[j] >= i-j) and dp[j] for j in range(h-1, i))
    total_teams = sum(1 for i in range(1, n+1) if s[h-1] >= i)
    
    if total_teams == 0:
        print(-1)
    else:
        prob = sum(dp[i] for i in range(1, n+1)) / total_teams
        print(prob)

if __name__ == "__main__":
    solve()
