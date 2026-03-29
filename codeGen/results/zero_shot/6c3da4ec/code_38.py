def max_bitwise_or(n, s):
    # Initialize maximum possible value to 0
    max_value = 0
    
    # Iterate over all possible cuts
    for i in range(1, n):
        # Calculate bitwise OR of two substrings
        left = int(s[:i], 2)
        right = int(s[i:], 2)
        
        # Update maximum possible value if needed
        max_value = max(max_value, left | right)
    
    # Convert the maximum possible value back to binary and remove leading zeroes
    return bin(max_value)[2:]
