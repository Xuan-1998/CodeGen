from collections import defaultdict

def min_height_of_bookcase(books, max_width):
    dp = [[0 for _ in range(max_width + 1)] for _ in range(len(books) + 1)]
    
    # Base case: when there are no books, the minimum height is 0
    dp[0] = [0] * (max_width + 1)
    
    memo = defaultdict(int)
    
    for i in range(1, len(books) + 1):
        for j in range(max_width + 1):
            if books[i - 1][0] > j:  # Book cannot fit on current shelf
                dp[i][j] = min(dp[i - 1][k] + books[i - 1][1] for k in range(j))
            else:
                dp[i][j] = min((dp[i - 1][k] if k >= books[i - 1][0] else float('inf')) + books[i - 1][1] for k in range(j, j - books[i - 1][0] + 1, -1))
    
    return dp[-1][-1]
