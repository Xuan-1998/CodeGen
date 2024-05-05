def max_bitwise_or(n, s):
    # Initialize max_sum and current_sum
    max_sum = 0
    current_sum = 0

    # Iterate through the binary string
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the bitwise OR of the two substrings
            or_value = int(s[i:j+1], 2)

            # Update current_sum
            current_sum += or_value

            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)

            # Reset current_sum for the next pair
            current_sum = 0

    return bin(max_sum)[2:]
