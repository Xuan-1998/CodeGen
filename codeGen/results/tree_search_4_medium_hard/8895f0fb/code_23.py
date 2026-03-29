import sys
from collections import defaultdict

def expected_non_zero_carries():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [defaultdict(int) for _ in range(N+1)]
        
        # Initialize base cases
        for i in range(10):
            dp[0][i] = 1
        
        # Fill up the DP table
        for n in range(1, N+1):
            for a in range(10):
                for b in range(10):
                    dp[n][a] += min(a+b, 9) - (min(a+b-10, 0))
        
        # Calculate the expected number of non-zero carries
        total_pairs = sum(sum([1 for _ in range(10)])**n for n in range(N+1))
        expected_carries = sum(sum([(a+b>=10)*1 for a in range(10) for b in range(10)])**(N-n) for n in range(N+1))
        
        # Print the result
        print(expected_carries / total_pairs)

expected_non_zero_carries()
