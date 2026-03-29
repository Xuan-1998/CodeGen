import sys

def min_height_of_bookcase(thicknesses, heights, max_shelf_width):
    n = len(thicknesses)
    dp = [[0] * (max_shelf_width + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(max_shelf_width + 1):
            if i == 0:
                dp[i][w] = max_shelf_width
            elif thicknesses[i - 1] <= w:
                min_height = min(dp[i - 1][w], heights[i - 1])
                dp[i][w] = min(min_height, dp[i - 1][w - thicknesses[i - 1]] + heights[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][max_shelf_width]

thicknesses = list(map(int, input().split()))
heights = list(map(int, input().split()))
max_shelf_width = int(input())

print(min_height_of_bookcase(thicknesses, heights, max_shelf_width))
