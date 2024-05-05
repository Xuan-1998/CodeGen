def max_bitwise_or(s):
    n = len(s)
    max_or = 0

    # Iterate over all possible pairs of non-empty substrings
    for i in range(n):
        for j in range(i + 1, n):
            left_int = int(s[:i], 2)
            right_int = int(s[i:j+1], 2)

            # Calculate the bitwise OR of their integer values
            or_val = left_int | right_int

            # Update the maximum value found so far
            max_or = max(max_or, or_val)

    return bin(max_or)[2:]  # Convert to binary and remove '0b' prefix

# Read input from stdin
n = int(input())
s = input()

print(max_bitwise_or(s))
