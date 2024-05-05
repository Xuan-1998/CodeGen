import sys

def solve():
    n, m, h = map(int, input().split())
    dp = [[0.0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        s = list(map(int, input().split()))
        
        for k in range(n+1):
            if k == 0:
                dp[i][k] = 1.0
            else:
                dp[i][k] = (1 - s[h-1]/(s[h-1]+sum(s[j:] for j in range(h)))) * sum(dp[j][min(k-j, n)] for j in range(i))
    
    ans = max((dp[m][n] if i >= h else 0.0) for i in range(m+1))
    print('%.6f' % (ans if ans > 0.0 else -1))

if __name__ == "__main__":
    solve()
