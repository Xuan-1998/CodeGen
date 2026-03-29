def solve():
    n = int(input())
    s = input()
    
    # Initialize dp with 0, since the bitwise OR of an empty string and itself is 0.
    dp = [0] * (n + 1)
    
    # For each character in s...
    for i in range(1, n + 1):
        # Calculate the maximum bitwise OR value by considering all possible pairs
        # of non-empty substrings that end at position i.
        for j in range(i):
            dp[i] = max(dp[i], dp[j - 1] | (int(s[j:i + 1], 2)))
    
    return bin(max(dp))[2:]

print(solve())
