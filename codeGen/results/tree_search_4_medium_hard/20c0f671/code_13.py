import sys

def min_height_of_bookcase():
    n, w = map(int, input().split())
    books = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(max(books[i-1][0], books[i-1][1]), w + 1):
            max_height = 0
            j = i
            while j > 0:
                if dp[j-1][w-books[i-1][0]] != 0:
                    max_height = max(max_height, dp[j-1][w-books[i-1][0]] + books[i-1][1])
                    j -= 1
                elif w - books[i-1][0] <= 0:
                    max_height = max(max_height, books[i-1][1])
                    break
                else:
                    j -= 1
            dp[i][w] = min(dp[i-1][w], max_height)
    
    return dp[n][w]

print(min_height_of_bookcase())
