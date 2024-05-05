def count_no_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        binary Representation = bin(i)[2:]  # Convert to binary and remove '0b' prefix
        has_consecutive_ones = False
        for j in range(len(binaryRepresentation) - 1):
            if binaryRepresentation[j] == '1' and binaryRepresentation[j + 1] == '1':
                has_consecutive_ones = True
                break
        if not has_consecutive_ones:
            count += 1
    return count

n = int(input())  # Read input from stdin
print(count_no_consecutive_ones(n))  # Print the answer to stdout
