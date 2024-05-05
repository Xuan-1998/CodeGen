import sys
from math import comb

def solve():
    n, m, h = map(int, input().split())
    dp = [[0.0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(m):
        if i == h-1:
            si = int(input()) + 1
        else:
            si = int(input())
        
        for j in range(n, -1, -1):
            dp[i+1][j] += (n-j) / n * (1 - (j-si)/n if si > 0 else 1)
    
    ans = 0.0
    for i in range(1, m+1):
        for j in range(max(0, n-m+i), -1, -1):
            ans += dp[i][j] * comb(n-j, i-1) / comb(n, i-1)
    
    print(ans)

if __name__ == "__main__":
    solve()
