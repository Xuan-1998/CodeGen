import sys

def solve():
    n = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split()))
    
    dp = [[0] * (n + 2) for _ in range(n + 1)]
    
    for i in range(1, n // 2 + 1):
        dp[i][i] = 1
        if p[i - 1] > i:
            dp[i][p[i - 1]] += 1
        else:
            dp[i][i - 1] += 1
    
    for i in range(n // 2 + 1, n + 1):
        dp[i][n + 1] = dp[n // 2][i - (n // 2)] + 1
        if p[i - 1] > i:
            dp[i][p[i - 1]] += 1
    
    print((dp[1][n + 1]) % (10**9 + 7))

if __name__ == "__main__":
    solve()
