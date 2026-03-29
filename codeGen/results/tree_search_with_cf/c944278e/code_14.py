def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Initialize the dp array
    dp = [[0] * (2**n) for _ in range(n + 1)]
    
    # Initial sequence is the permutation of integers from 1 to 2^n
    for j in range(2**n):
        dp[0][j] = j + 1
    
    # Fill the dp array based on the given binary string s
    for i in range(n):
        for j in range(2**(n - i - 1)):
            if s[i] == '0':
                dp[i + 1][j] = min(dp[i][2 * j], dp[i][2 * j + 1])
            else:
                dp[i + 1][j] = max(dp[i][2 * j], dp[i][2 * j + 1])
    
    # The result is the unique values found in dp[n][0]
    result = set(dp[n])
    
    # Output the result in ascending order
    print(' '.join(map(str, sorted(result))))


