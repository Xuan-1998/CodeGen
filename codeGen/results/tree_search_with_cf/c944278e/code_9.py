python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    from collections import defaultdict
    
    # Initialize dp array with sets
    dp = [defaultdict(set) for _ in range(n + 1)]
    
    # Base case: initial values
    for i in range(1, 2**n + 1):
        dp[0][i].add(i)
    
    # Transition
    for i in range(1, n + 1):
        for mask in range(1, 2**n + 1):
            bit = s[i - 1]
            if bit == '0':  # Keep the smaller one
                for j in range(1, 2**n + 1, 2):
                    if j + 1 <= 2**n:
                        dp[i][mask].update(min(a, b) for a in dp[i - 1][j] for b in dp[i - 1][j + 1])
            else:  # Keep the larger one
                for j in range(1, 2**n + 1, 2):
                    if j + 1 <= 2**n:
                        dp[i][mask].update(max(a, b) for a in dp[i - 1][j] for b in dp[i - 1][j + 1])
    
    # Final state
    full_mask = (1 << n) - 1
    result = sorted(dp[n][full_mask])
    
    # Print result
    print(" ".join(map(str, result)))


