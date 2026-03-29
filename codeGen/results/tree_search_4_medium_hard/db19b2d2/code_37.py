import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [[0.0 for _ in range(n+1)] for _ in range(m+1)]
    
    dp[0][0] = 1.0
    
    for i in range(1, m+1):
        for k in range(n+1):
            if k < h:
                for j in range(h):
                    dp[i][k] += (s[i-1] - j) / sum(s) * dp[i-1][k]
            else:
                for j in range(min(h, s[i-1])):
                    dp[i][h] += (s[i-1] - j) / sum(s) * dp[i-1][k]
    
    result = 1.0 - dp[m][n]
    
    print("%.6f" % result)

if __name__ == "__main__":
    solve()
