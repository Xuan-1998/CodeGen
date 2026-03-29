import sys
from collections import defaultdict

def min_height_of_bookshelf():
    n, w = map(int, input().split())
    books = []
    for _ in range(n):
        thickness, height = map(int, input().split())
        books.append((thickness, height))
    
    dp = [[0] * (w+1) for _ in range(n+1)]
    
    # Initialize the first row of the table
    for j in range(w+1):
        dp[0][j] = 0
    
    for i in range(1, n+1):
        for w in range(w, books[i-1][0]-1, -1):  # From max shelf width down to current book's thickness
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-books[i-1][0]] + books[i-1][1])
    
    return min(dp[-1])

print(min_height_of_bookshelf())
