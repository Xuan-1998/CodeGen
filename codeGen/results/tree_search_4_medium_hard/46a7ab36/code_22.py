import sys

def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        k = (10**8 + 7)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base case
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            dp[i][0] = 1
            
        for j in range(1, m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            elif j == 1 and i < 2 * n:
                dp[i][j] = n
            else:
                if i >= 2 * n:
                    dp[i][j] = (k - i + 1) % k
                else:
                    dp[i][j] = (dp[2 * i % k][j - 1] + (i < k)) % k
        
        print((dp[n][m]) % k)

if __name__ == "__main__":
    solve()
