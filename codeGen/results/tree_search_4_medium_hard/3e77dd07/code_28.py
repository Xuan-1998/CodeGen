def is_scrambled(s1, s2):
    n = len(s1)
    
    # Initialize the dp table with False values
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Handle edge cases
    if n == 0:
        return True
    
    for i in range(n):
        if s1[i] != s2[i]:
            return False
    
    # Fill the dp table using dynamic programming
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            for k in range(length):
                if s1[i+k] != s2[j-k]:
                    break
            else:
                dp[i][j] = (dp[0][k-1] and dp[k][j-1])
                
    # Return the result based on the filled dp table
    return dp[0][n - 1]

# Example usage
s1 = input()
s2 = input()

if is_scrambled(s1, s2):
    print("True")
else:
    print("False")

