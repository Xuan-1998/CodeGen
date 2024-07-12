python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Initialize dp table
    dp = [[set() for _ in range(2**(n-i))] for i in range(n+1)]
    
    # Base case: subarrays of length 1
    for j in range(2**n):
        dp[0][j] = {j + 1}
    
    # Fill dp table
    for i in range(1, n+1):
        for j in range(2**(n-i)):
            if s[n-i] == '0':
                dp[i][j] = {min(x, y) for x in dp[i-1][2*j] for y in dp[i-1][2*j+1]}
            else:  # s[n-i] == '1'
                dp[i][j] = {max(x, y) for x in dp[i-1][2*j] for y in dp[i-1][2*j+1]}
    
    # The result is the sorted list of values in dp[n][0]
    result = sorted(dp[n][0])
    print(' '.join(map(str, result)))


