def solve():
    n = int(input())
    p = list(map(int, input().split()))
    
    dp = [[False] * (n + 1) for _ in range(2 * n + 1)]
    
    for i in range(1, 2 * n + 1):
        if i % 2 == 0:
            j = n
            while j >= 0 and p[i - 1] != p[i // 2]:
                j -= 1
            dp[i][j + 1] = True
        else:
            for j in range(n, -1, -1):
                if p[i - 1] == p[i // 2]:
                    dp[i][j] = False
                    break
                elif j > 0 and p[i - 1] < p[i // 2]:
                    dp[i][j] = dp[i - 1][j]
                    break
                else:
                    dp[i][j] = True
    
    print("YES" if dp[2 * n][n] else "NO")

if __name__ == "__main__":
    solve()
