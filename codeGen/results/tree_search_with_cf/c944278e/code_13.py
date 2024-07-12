python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Initialize dp with 2^n rows and n+1 columns
    dp = [[0] * (2**n) for _ in range(n + 1)]
    
    # Base case
    for j in range(2**n):
        dp[0][j] = j + 1
    
    # Fill dp table
    for i in range(1, n + 1):
        for j in range(2**(n - i)):
            if s[i - 1] == '0':
                dp[i][j] = min(dp[i - 1][2 * j], dp[i - 1][2 * j + 1])
            else:
                dp[i][j] = max(dp[i - 1][2 * j], dp[i - 1][2 * j + 1])
    
    # Collect results from the final level
    result = set()
    for j in range(2**(n - n)):
        result.add(dp[n][j])
    
    # Sort and print the results
    print(' '.join(map(str, sorted(result))))


