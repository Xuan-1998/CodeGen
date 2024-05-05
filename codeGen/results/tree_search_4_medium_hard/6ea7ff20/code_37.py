import sys

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    dp[0][n] = True
    
    for i in range(1, n):
        for j in range(i, n):
            if p[2*i-1] < p[2*j-1]:
                dp[i][j] = (dp[i-1][j] or dp[i][j-1]) and p[2*i-1] < p[2*j]
            elif p[2*i-1] >= p[2*j-1]:
                dp[i][j] = dp[max(i, j)]
    
    print('YES' if dp[n-1][n-1] else 'NO')

if __name__ == "__main__":
    solve()
