def count_words(n, m):
    dp = [[0] * (m + 1) for _ in range((n + 1) // 2)]
    
    # Base case: when i == 0 and j == m, there is only one way to form the word
    dp[0][m] = 1
    
    for i in range(1, (n + 1) // 2):
        for j in range(m - 1, -1, -1):
            if i < n:
                # When i < n/2, we have more flexibility in placing letters
                dp[i][j] = (dp[i][j + 1] * (n - 1) + 
                            ((i < n / 2) and j == m - 1 or 
                             ((n - i - 1) * 2) % n != 0) * 
                            dp[(n - i - 1) // 2][m - j - 1]) % (10**8 + 7)
            else:
                # When i >= n/2, we have fewer options
                if j == m - 1 or ((n - i - 1) * 2) % n != 0:
                    dp[i][j] = (dp[(n - i - 1) // 2][m - j - 1]) % (10**8 + 7)
    
    return dp[-1][-1]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(count_words(n, m))
