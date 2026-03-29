from sys import stdin

def count_possible_words():
    t = int(stdin.readline())
    for _ in range(t):
        n, m = map(int, stdin.readline().split())
        dp = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            if i % 2 == 0:
                dp[i][0] = 1
            else:
                dp[i][0] = n - i
            for j in range(1, m + 1):
                if (i + 1) % 2 != 0 and j > 0:
                    dp[i][j] = dp[(i + 1) % n][j - 1]
                else:
                    dp[i][j] = dp[i][m - j]
        print((dp[0][m]) % (10**8 + 7))

count_possible_words()
