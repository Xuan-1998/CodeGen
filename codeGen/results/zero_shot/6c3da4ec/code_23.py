def max_bitwise_or(n, s):
    max_or = 0

    # Iterate over all possible pairs of non-empty substrings
    for i in range(1, n):
        for j in range(i + 1, n):
            # Calculate the bitwise OR of the current pair of substrings
            or_value = int(s[:i], 2) | int(s[i:j], 2)

            # Update the maximum bitwise OR found so far
            max_or = max(max_or, or_value)

    return bin(max_or)[2:]

# Read input from stdin
n = int(input())
s = input()

# Calculate and output the maximum possible value
print(max_bitwise_or(n, s))
