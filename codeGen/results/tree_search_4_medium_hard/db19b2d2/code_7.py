from math import comb

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    if sum(s) < n:
        print(-1)
        return
    
    dp = [[0.0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, min(i, n) + 1):
            if i == h:
                dp[i][j] = comb(s[i - 1], j - 1) / comb(sum(s), j)
            else:
                dp[i][j] = sum(dp[k][j - 1] * (k != h) for k in range(1, i + 1))
    
    print(dp[m][n])

if __name__ == "__main__":
    solve()
