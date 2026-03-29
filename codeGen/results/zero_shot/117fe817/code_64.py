def count_digit_ones(n):
    # Count numbers ending with 1
    ones = n // 10
    
    # Initialize total count
    total_count = 0
    
    # Loop through each digit (from 1 to n % 10)
    for i in range(1, n % 10 + 1):
        # Add the count of numbers ending with i
        total_count += (n - i * 10) // 10
    
    # Return the total count
    return ones + total_count

# Read input from stdin
n = int(input())

# Calculate and print the answer
print(count_digit_ones(n))
