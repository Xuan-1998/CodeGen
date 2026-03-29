import sys

def max_bitwise_or(n, s):
    # Initialize the maximum value to 0
    max_value = 0
    
    # Iterate over all possible pairs of substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            # Convert each substring to an integer and perform a bitwise OR operation
            value = int(s[i:j+1], 2) | int(s[j+1:], 2)
            
            # Update the maximum value if the current value is greater
            max_value = max(max_value, value)
    
    return bin(max_value)[2:]  # Remove the '0b' prefix and return the binary representation

# Read input from stdin
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

# Call the function and print the output to stdout
print(max_bitwise_or(n, s))
