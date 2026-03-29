import math

def count_digit_ones(n):
    total_ones = 0
    for i in range(math.floor(math.log10(n)) + 1):
        # Calculate the number of integers with i digits
        num_ints = 10 ** i - 1
        
        # For each integer, calculate the number of times digit 1 appears
        ones_per_int = (10 ** (i + 1) - 1) // 9 * 8 + (n >= 10 ** i)
        
        # Add the total number of ones for this many integers
        total_ones += num_ints * ones_per_int
    
    return total_ones

n = int(input())  # Read input from stdin
print(count_digit_ones(n))  # Print output to stdout
