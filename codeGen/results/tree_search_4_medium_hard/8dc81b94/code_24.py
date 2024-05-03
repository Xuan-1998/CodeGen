import sys

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        dp = [[False] * (n+1) for _ in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n+1):
            for j in range(min(i, n)+1):
                if arr[i-1] <= 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
        
        print("YES" if dp[n][n//2] else "NO")

if __name__ == "__main__":
    solve()
