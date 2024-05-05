def count_binary_no_consecutive_ones(n):
    count = 0
    for i in range(n+1):
        bin_i = bin(i)[2:]  # Convert integer to binary and remove '0b' prefix
        has_consecutive_ones = False
        for j in range(len(bin_i)-1):  # Check each pair of bits
            if bin_i[j] == '1' and bin_i[j+1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1
    return count

n = int(input())  # Read input from stdin
print(count_binary_no_consecutive_ones(n))  # Print output to stdout
