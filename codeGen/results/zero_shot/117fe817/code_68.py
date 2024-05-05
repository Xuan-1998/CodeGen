def count_ones(n):
    total_ones = 0
    for i in range(n + 1):
        bi = bin(i)[2:]  # Convert integer to binary and remove '0b' prefix
        total_ones += bi.count('1')  # Count the number of ones in the binary representation
    return total_ones

n = int(input())  # Read input from stdin
print(count_ones(n))  # Print the result to stdout
