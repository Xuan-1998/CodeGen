for i in range(n + 1):
    bin_i = bin(i)[2:]  # Convert i to binary representation
    has_consecutive_ones = False
    for j in range(len(bin_i) - 1):  # Check each pair of bits
        if bin_i[j] == '1' and bin_i[j + 1] == '1':
            has_consecutive_ones = True
            break
    if not has_consecutive_ones:
        count += 1

# Print the output to stdout
print(count)
