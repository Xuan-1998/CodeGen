import sys

def alien_words():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Initialize base cases: single-letter words
        for i in range(1, n + 1):
            dp[i][1] = 1
        
        # Fill up the table using dynamic programming
        for i in range(2, n + 1):
            for j in range(2, min(i, m) + 1):
                if i % 2 == 0:
                    dp[i][j] = (dp[i // 2][j - 1] * (i // 2)) % (10**8 + 7)
                else:
                    dp[i][j] = sum(dp[k][j - 1] for k in range(1, i)) % (10**8 + 7)
        
        print(dp[n][m])

if __name__ == "__main__":
    alien_words()
