def count_non_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        binary = bin(i)[2:]  # Convert integer to binary and remove '0b' prefix
        has_consecutive_ones = False
        for j in range(len(binary) - 1):
            if binary[j] == '1' and binary[j + 1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1
    return count

# Read input from stdin
n = int(input())

# Print the result to stdout
print(count_non_consecutive_ones(n))
