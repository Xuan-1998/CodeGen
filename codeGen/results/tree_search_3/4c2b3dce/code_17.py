def solve():
    s = input()
    n = len(s)
    
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(i + 1):
            if s[j:i].endswith("AB") or s[j:i].endswith("BA"):
                dp[i][j] = True
                if i > j:
                    dp[i][j] &= dp[i-1][j+2]
    
    print("YES" if any(any(dp[i][j]) for i in range(n + 1)) else "NO")

if __name__ == "__main__":
    solve()
