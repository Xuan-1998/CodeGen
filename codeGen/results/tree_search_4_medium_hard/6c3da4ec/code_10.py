from collections import defaultdict

def max_OR(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Initialize the base case
    for i in range(n+1):
        dp[i][i] = 0
    
    memo = defaultdict(int)
    
    for j in range(1, n+1):
        for i in range(j-1, -1, -1):
            if i == j-1:
                dp[i][j] = int(s[i], 2)
            else:
                max_val = 0
                for k in range(i+1, j):
                    bit_or = int(s[k:j], 2) | int(s[i:k], 2)
                    dp[i][j] = max(dp[i][j], bit_or)
    
    # Calculate the maximum value in the last row of the DP table
    return format(max((dp[0][n-1])), 'b').count('1')

# Read input from stdin and write output to stdout
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    
    print(max_OR(s))
