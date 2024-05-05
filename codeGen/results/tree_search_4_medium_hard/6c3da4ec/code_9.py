def maxOr(s):
    n = len(s)
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Base case when j-i is 0 or 1: 
    # There's only one possible substring, so consider the last character(s) in that range
    for i in range(n):
        dp[i][i+1] = int(s[i])
        
    # Recursive case
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length
            max_or = 0
            for k in range(i+1, j):
                or_value = dp[i][k] | dp[k][j]
                max_or = max(max_or, or_value)
            dp[i][j] = max_or
    
    # Return the maximum bitwise OR value found
    return bin(dp[0][n-1])[2:]

# Read input from stdin and write output to stdout
if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    print(maxOr(s))
