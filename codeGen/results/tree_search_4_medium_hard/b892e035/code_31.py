import sys
from math import comb

# Read input from stdin
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    p1, num1, num2 = [int(x) for x in sys.stdin.readline().split()]
    
    # Initialize the dp table with zeros
    dp = [[0.0] * (16 + 1) for _ in range(n + 1)]
    
    # Base case: For the first ticket, there's only one way to number it correctly
    dp[0][num1] = p1
    
    # Fill up the dp table using dynamic programming
    for i in range(1, n):
        for j in range(16 + 1):
            if comb(i - 1, j) > 0:
                dp[i][j] = (dp[i - 1][max(0, j - 1)] * (num2 == j) + 
                            dp[i - 1][min(15, j + 1)] * (num1 == j)) / comb(i, j)
    
    # The answer is the sum of probabilities for all possible numberings
    total_prob = sum(prob for prob in dp[-1])
    
    print('%.6f' % total_prob)

