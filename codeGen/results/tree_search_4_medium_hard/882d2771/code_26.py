import sys

def beauty_contest():
    t, l, r = map(int, input().split())
    
    # Base case: dp[i] = 0 for all i
    dp = [0] * (r + 1)
    
    # Calculate the value of f(n) for n from l to r
    for n in range(l, r + 1):
        # Initialize the minimum total number of pairwise comparisons needed
        min_total_comparisons = sys.maxsize
        
        # For each possible combination of t0, t1, ..., tr:
        for i in range(t + 1):
            for j in range(i):
                if (n - l) * (i * (2**j)) % (10**9 + 7) < min_total_comparisons:
                    min_total_comparisons = (n - l) * (i * (2**j)) % (10**9 + 7)
        
        # Update dp[n] with the minimum total number of pairwise comparisons needed
        dp[n] = min_total_comparisons
    
    return dp[r]

print(beauty_contest())
