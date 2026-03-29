import sys
from collections import defaultdict

def expected_non_zero_carries():
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        
        # Initialize the DP table with base cases
        dp = [[0, 1] for _ in range(N+1)]
        
        # Iterate through each digit from n = N down to n = 1
        for i in range(1, N+1):
            carry_count = defaultdict(int)
            
            # For each possible value of A and B at the current digit
            for a in range(10):
                for b in range(10):
                    # Calculate the expected number of non-zero carries based on whether there was a carry from the previous addition
                    if i > 1:
                        carry_count[dp[i-1][1]] += 1
                    else:
                        carry_count[0] += 1
            
            # Update the DP table for the current digit
            dp[i] = [carry_count.get(0, 0), sum(carry_count.values())]
        
        # Return the value stored in the DP table for the initial state (0, 0)
        print(dp[0][0]/sum(range(1, 11)) * N)

if __name__ == "__main__":
    expected_non_zero_carries()
