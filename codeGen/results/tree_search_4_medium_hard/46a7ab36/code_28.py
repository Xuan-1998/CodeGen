[

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n)]

    # Base case: There is only one way to form a word of length 0.
    for j in range(m + 1):
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(m + 1):
            if i % 2 == 0:
                # If the index is even, a letter can be placed at any position.
                dp[i][j] = (i == 0 or i % 2 != 0) and dp[(i - 1) % n][j]
            else:
                # If the index is odd, a letter can be placed only after the previous letter.
                if j < m:
                    dp[i][j] = (i == 0 or i % 2 != 0) and dp[(i - 1) % n][j - 1]
                else:
                    # If we're at the end of the word, a letter can be placed only after the previous letter.
                    dp[i][j] = dp[(i - 1) % n][m - 1] + (i < n) and dp[(i - 1) % n][j]

    print((dp[-1][-1]) % (10**8 + 7))

]
