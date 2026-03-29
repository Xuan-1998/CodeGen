import sys
from collections import defaultdict

def solve():
    t = int(input())
    dp = defaultdict(int)
    
    # Initialize base case
    for k in range(1, 10):
        dp[0][k] = k
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        # Compute the result for each possible state
        for i in range(m+1):
            if i == 0:
                val = n
            else:
                val = (val % 10) * (10 ** (i-1)) + ((val // 10) + 1)
            
            # Update dp[i][j] with the minimum length of the resulting number after i operations when the initial number is j
            for k in range(10):
                if val % 10 == k+1 or val // 10 == k+1:
                    dp[i][k] = min(dp[i-1].get(k, float('inf')), dp[i][k])
        
        # Compute and print the final answer
        sys.stdout.write(str(min(dp[m].values())) + '\n')

if __name__ == '__main__':
    solve()
