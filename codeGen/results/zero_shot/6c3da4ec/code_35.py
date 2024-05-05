def max_bitwise_or(n, s):
    # Create a prefix sum array to store the cumulative bitwise OR values
    ps = [0]
    for c in s:
        ps.append(ps[-1] | int(c))

    max_or = 0

    # Iterate over all pairs of non-empty substrings
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the bitwise OR of the current pair's integer values
            or_val = ps[j + 1] - ps[i]
            max_or = max(max_or, or_val)

    return bin(max_or)[2:]
