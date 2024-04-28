import sys

def solve():
    m, n = map(int, input().split())
    dp = {0: 1}
    
    for i in range(m):
        for j in range(n+1):
            if j not in dp:
                dp[j] = 0
            if j - (i+1) >= 0 and j - (i+1) in dp:
                dp[j] += dp[j-(i+1)]
        dp[n] %= (10**9 + 7)
    print(dp.get(n, 0))

if __name__ == "__main__":
    solve()
