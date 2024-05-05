def max_bitwise_or(s):
    n = len(s)
    
    # Initialize 2D DP table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Iterate over the binary string from left to right
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # Calculate the maximum bitwise OR value for any substring of length j ending at index i
            dp[i][j] = max(dp[i][j], s[i] | dp[i + 1][j])
    
    # Find the maximum bitwise OR value by iterating over all possible lengths j of the substring and taking the maximum
    return max(max(dp[i]) for i in range(n))

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(max_bitwise_or(s))
