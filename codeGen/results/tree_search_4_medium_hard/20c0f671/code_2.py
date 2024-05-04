import sys

def min_height_of_bookcase():
    n, m = map(int, input().split())  # number of books, max shelf width
    heights = list(map(lambda x: list(map(int, x.split())), (input().split('\n'))[:-1]))  # list of book sizes
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(m + 1):
            if heights[i-1][0] > w:  # current book can't fit on the shelf
                dp[i][w] = dp[i-1][w]
            else:
                # calculate maximum height of shelf and update dp[i][w]
                max_height = max(heights[j-1][1] for j in range(i+1) if heights[j-1][0] <= w)
                dp[i][w] = min(dp[i-1][w], max_height)

    return dp[n][m]

print(min_height_of_bookcase())
