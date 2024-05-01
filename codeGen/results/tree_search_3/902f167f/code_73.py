from collections import namedtuple
from math import sqrt

Rect = namedtuple('Rect', ['n', 'm'])

def min_squares(rect):
    n, m = rect.n, rect.m
    
    # Create a dictionary to store the computed values of dp[i][j]
    memo = {}
    
    def dp(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Find the maximum side length of a square that can be placed at the top or left of the rectangle
        max_side = min(i, j)
        res = float('inf')
        
        for k in range(1, max_side+1):
            if i >= k and j >= k:
                res = min(res, dp(k, k) + (i-k)*(j-k))
        
        memo[(i, j)] = res
        
        return res
    
    return dp(n, m)

# Test the function
rect = Rect(*map(int, input().split()))
print(min_squares(rect))
