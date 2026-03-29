def count_numbers_without_consecutive_ones(n):
    count = 0
    for i in range(n + 1):
        binary = bin(i)[2:]  # Convert integer to binary string, removing '0b' prefix
        has_consecutive_ones = False
        run_count = 0
        for char in binary:
            if char == '1':
                run_count += 1
                if run_count > 1:  # Found a run of consecutive ones
                    has_consecutive_ones = True
                    break
            else:
                run_count = 0
        if not has_consecutive_ones:
            count += 1
    return count

n = int(input())  # Read input from stdin
print(count_numbers_without_consecutive_ones(n))  # Print the result to stdout
