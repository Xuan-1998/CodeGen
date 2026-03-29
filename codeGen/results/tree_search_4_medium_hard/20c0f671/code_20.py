import sys

def min_height_of_bookcase():
    n, w = map(int, input().split())
    books = []
    for _ in range(n):
        t, h = map(int, input().split())
        books.append((t, h))
    
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for k in range(w + 1):
            if books[i - 1][0] <= k:
                dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - books[i - 1][0]] + books[i - 1][1])
            else:
                dp[i][k] = dp[i - 1][k]
    
    return dp[n][w]

print(min_height_of_bookcase())
