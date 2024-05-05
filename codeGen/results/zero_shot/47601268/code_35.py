def count_binary_strings(n):
    count = 0

    for i in range(n + 1):
        binary_str = bin(i)[2:]  # Convert integer to binary string, removing '0b' prefix

        has_consecutive_ones = False
        prev_bit = None

        for bit in binary_str:
            if bit == '1':
                if prev_bit == '1':  # If the previous bit was also 1, we have consecutive ones
                    has_consecutive_ones = True
                    break
            prev_bit = bit

        if not has_consecutive_ones:  # Increment the count only if there are no consecutive ones
            count += 1

    return count
